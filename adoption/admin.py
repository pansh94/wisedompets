from django.contrib import admin

from .models import Pets


#to determine the model it is associated with there fore Pets is passed
@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex']
