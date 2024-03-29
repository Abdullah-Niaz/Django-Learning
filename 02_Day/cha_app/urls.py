from django.urls import path
from . import views

urlpatterns = [
    path("junvary", views.junvary),
    path('weAreDone',views.weAreDone)
]
