from django.urls import path
from . import views

urlpatterns = [
    path("",views.fee_home)
]
