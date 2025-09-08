from django.shortcuts import render

def index(request):
    return render(request, "pos/index.html")

def home(request):
    return render(request, "pos/home.html")

def category(request):
    return render(request, "pos/category.html")

def sales(request):
    return render(request, "pos/sales.html")

def report(request):
    return render(request, "pos/report.html")

def units(request):
    return render(request, "pos/units.html")

def products(request):  
    return render(request, "pos/products.html")
