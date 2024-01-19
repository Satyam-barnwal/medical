from django.contrib import admin

# Register your models here.
from .models import Doctor, Patient, AppointmentDetails,Contact
@admin.register(Patient)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['username','name','mob_no','email']

@admin.register(Doctor)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['name','desc','exp']

@admin.register(AppointmentDetails)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['name','mob_no','email','consultant','date','slot']

@admin.register(Contact)
class ConttactModelAdmin(admin.ModelAdmin):
    list_display=['name']