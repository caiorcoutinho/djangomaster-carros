from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarModelForm
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/'

class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars = cars.filter(
                Q(brand__name__icontains=search) | Q(model__icontains=search) | Q(factory_year__contains=search) | Q(model_year__contains=search)
            )
        
        return render(
            request, 
            'cars.html', 
            { 'cars': cars },
        )


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(
                Q(brand__name__icontains=search) | Q(model__icontains=search) | Q(factory_year__contains=search) | Q(model_year__contains=search)
            )
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = "/"


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = "/"