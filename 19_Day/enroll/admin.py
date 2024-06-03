from django.contrib import admin

from enroll.models import *
# Register your models here.


@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ("id","stuid","stuName","stuAddress","stuMessage")

# admin.site.register(student,studentAdmin)