from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.formFunc),
    path("success/", views.showFormSubmission, name="")
]
