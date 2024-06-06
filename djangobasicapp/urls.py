from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("Home", views.Home, name="Home"),
    path("ShowMessages", views.ShowMoreMessage, name="ShowMoreMessage"),
    path("UseVariables", views.UseVariableAsResponse, name="UVR"),
    path("GetRequestDemo", views.GetRequestVariables, name="GRV"),
    path("ShowTime", views.ShowDateTimeInfo, name="SDTI"),
    path("ifTagDemo", views.iftagdemo, name="ITD"),
    path("showProducts", views.ShowProducts, name="SP"),


]



