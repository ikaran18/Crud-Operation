from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','roll_id')

