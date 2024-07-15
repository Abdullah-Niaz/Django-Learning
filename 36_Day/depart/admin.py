from django.contrib import admin
from .models import StudentInfo

# Register your models here.
@admin.register(StudentInfo)


class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'roll', 'marks','pass_date' )


# admin.site.register(StudentInfo,StudentInfoAdmin)