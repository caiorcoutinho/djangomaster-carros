from django.contrib import admin
from cars.models import Brand, Car

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def __str__(self):
        return self.name
    
admin.site.register(Brand, BrandAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value',)
    search_fields = ('model', 'brand',)

admin.site.register(Car, CarAdmin)

