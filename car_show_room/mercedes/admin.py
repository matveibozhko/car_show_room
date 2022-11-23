from django.contrib import admin
from car_show_room.mercedes.models import Car, Provider


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'provider', 'price']
    list_filter = ['mark_startswith']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email']
    list_filter = ['company_name']
