from django.urls import path
from . import views

urlpatterns = [
    path("",views.fee_home),
    path("feeplans/",views.feeplans),
    path("relaxation/",views.relaxation),
    path("feestructure/",views.feestructure,name="feestructure")
]
