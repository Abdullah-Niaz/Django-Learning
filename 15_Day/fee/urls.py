from django.urls import path
from . import views
urlpatterns = [
    path("feehome/",views.feehome)
]