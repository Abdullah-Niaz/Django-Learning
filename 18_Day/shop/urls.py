from django.urls import path
from . import views


urlpatterns = [
    path("shop/", views.shop,name="shop"),
    path("shopdashboard/", views.shopdashboard,name="shopdashboard")
]
