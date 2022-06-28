from django.urls import path
from . import views

urlpatterns = [
    path("", views.Datefilter, name='csv'),
    path("filter/", views.Readcsv, name='filter'),
    path("export_to_csv/", views.Generate_csv, name='export_to_csv'),
    
]