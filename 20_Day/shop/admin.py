from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StudentData)

class studentDataAdmin(admin.ModelAdmin):
    list_display = ['name','roll_no','stuid']

# admin.site.register(StudentData,studentDataAdmin)