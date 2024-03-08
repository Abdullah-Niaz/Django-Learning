from django.urls import path
from . import views

urlpatterns = [
    # dynaic method 
    # Dynamic Path Segments & Captured Values
    path("<int:route>/",views.dynamic_int),
    path("<str:route>/", views.dynamic, name="")
]
