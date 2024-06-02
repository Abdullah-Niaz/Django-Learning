from django.contrib import admin
from shop.models import student
# Register your models here.


@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ("id","stuid","stuName","stuAddress","stuMessage")