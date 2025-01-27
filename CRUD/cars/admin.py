from django.contrib import admin
from cars.models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_name', 'car_model', 'car_speed')