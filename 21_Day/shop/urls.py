from django.urls import path,include
from .  import views

app_name = 'shop'  # Define the app namespace

urlpatterns = [
    path('fee/', views.fee, name='fee'),
    path('fee-structure/', views.feestructure, name='feestructure'),
]