from django.urls import path
from . import views


urlpatterns = [
   path("<int:route>/",views.dynamic_int),
    path("<str:route>/", views.dynamic_str)
]