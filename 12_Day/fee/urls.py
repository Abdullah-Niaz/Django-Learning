from django.urls import path
from . import views

urlpatterns = [
    path("fee/", views.fee),
    path("<int:route>/",views.dynamic)
]
