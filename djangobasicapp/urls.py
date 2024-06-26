from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="Index"),
    path("Index", views.Index, name="Index"),
    path("Home", views.Home, name="Home"),
    path("ShowMessages", views.ShowMoreMessage, name="ShowMoreMessage"),
    path("UseVariables", views.UseVariableAsResponse, name="UVR"),
    path("GetRequestDemo", views.GetRequestVariables, name="GRV"),
    path("ShowTime", views.ShowDateTimeInfo, name="SDTI"),
    path("ifTagDemo", views.iftagdemo, name="ITD"),
    path("showProducts", views.ShowProducts, name="SP"),
    path("showUsers", views.LoadUsers, name="LoadUsers"),
    path("showUsersAsCard", views.LoadUsers2, name="LoadUsers2"),
    path("showUserDetails", views.LoadUserDetails, name="ShowUsersDetails"),
    path("PassModel", views.PassModelTotemplate, name="PMT"),
    path("BIFDemo", views.BuiltInFiltersDemo, name="BIFD"),
    path("TestCustomFilters", views.CustomFiltersDemo, name="CFD"),
    path("TestStaticFiles", views.TestStaticFiles, name="TSF"),




]



