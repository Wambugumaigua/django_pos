from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),           
    path("home/", views.home, name="home"),
    path("category/", views.category, name="category"),
    path("sales/", views.sales, name="sales"),
    path("report/", views.report, name="report"),
    path("units/", views.units, name="units"),
    path("products/", views.products, name="products"),  
]
