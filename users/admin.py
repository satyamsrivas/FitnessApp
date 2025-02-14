from django.contrib import admin
from .models import User,FitnessProfile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','mobile_number']
    search_fields = ['first_name','mobile_number']

class FitnessProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','created_at']
    list_fields = ["user","gender","height","weight","bmi"]
    list_filter = ['gender']

admin.site.register(User,UserAdmin)
admin.site.register(FitnessProfile,FitnessProfileAdmin)
