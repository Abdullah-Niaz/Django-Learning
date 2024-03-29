from . import views
from django.urls import path

urlpatterns = [

    path("contact/",views.contact),
    path("<route>/",views.dynamic_function),
    path("contact/<str:employee_id>/", views.contactinside, name='home')
]
