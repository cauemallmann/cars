from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'car_type', 'value')
    search_fields = ('model',)
    #list_filter = ('factory_year', 'brand', 'car_type', 'value')
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)    
    
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
