from django.contrib import admin
from cars.models import Brand, Car

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    
admin.site.register(Brand, BrandAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo', 'plate',)
    search_fields = ('model', 'brand',)

admin.site.register(Car, CarAdmin)

