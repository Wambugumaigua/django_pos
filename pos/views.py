from django.shortcuts import render
from django.utils.text import slugify
from django.http import JsonResponse
from .models import Category

# ----- Pages -----
def index(request):
    return render(request, "pos/index.html")

def home(request):
    return render(request, "pos/home.html")

def sales(request):
    return render(request, "pos/sales.html")

def report(request):
    return render(request, "pos/report.html")

def signin(request):
    return render(request, "pos/signin.html")  # 👈 added signin view


# ----- Units -----
dynamic_units = []  # Temporary in-memory store

def units(request):
    return render(request, "pos/units.html", {"units": dynamic_units})

def add_unit(request):
    if request.method == "POST":
        unit_name = request.POST.get("unit_name")
        short_name = request.POST.get("short_name")
        new_id = max([u["id"] for u in dynamic_units], default=0) + 1
        unit = {
            "id": new_id,
            "unit_name": unit_name,
            "short_name": short_name,
        }
        dynamic_units.append(unit)
        return JsonResponse({"success": True, "unit": unit})
    return JsonResponse({"error": "Invalid request"}, status=400)

def edit_unit(request, unit_id):
    if request.method == "POST":
        unit = next((u for u in dynamic_units if u["id"] == unit_id), None)
        if unit:
            unit["unit_name"] = request.POST.get("unit_name")
            unit["short_name"] = request.POST.get("short_name")
            return JsonResponse({"success": True, "unit": unit})
        return JsonResponse({"error": "Unit not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_unit(request, unit_id):
    if request.method == "POST":
        global dynamic_units
        dynamic_units = [u for u in dynamic_units if u["id"] != unit_id]
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid request"}, status=400)


# ----- Products -----
example_products = []  # Temporary in-memory store

def products(request):
    return render(request, "pos/products.html", {"products": example_products})

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        brand = request.POST.get("brand")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        type_ = request.POST.get("type")
        owner = request.POST.get("owner")
        new_id = max([p["id"] for p in example_products], default=0) + 1
        product = {
            "id": new_id,
            "name": name,
            "category": category,
            "brand": brand,
            "price": price,
            "stock": stock,
            "type": type_,
            "owner": owner,
        }
        example_products.append(product)
        return JsonResponse({"success": True, "product": product})
    return JsonResponse({"error": "Invalid request"}, status=400)

def edit_product(request, product_id):
    if request.method == "POST":
        product = next((p for p in example_products if p["id"] == product_id), None)
        if product:
            product.update({
                "name": request.POST.get("name"),
                "category": request.POST.get("category"),
                "brand": request.POST.get("brand"),
                "price": request.POST.get("price"),
                "stock": request.POST.get("stock"),
                "type": request.POST.get("type"),
                "owner": request.POST.get("owner"),
            })
            return JsonResponse({"success": True, "product": product})
        return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_product(request, product_id):
    if request.method == "POST":
        global example_products
        example_products = [p for p in example_products if p["id"] != product_id]
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid request"}, status=400)

def product_details(request, product_id):
    product = next((p for p in example_products if p["id"] == product_id), None)
    if product:
        return JsonResponse({"success": True, "product": product})
    return JsonResponse({"error": "Product not found"}, status=404)


# ----- Categories -----
def category(request):
    categories = Category.objects.all().order_by("-created_on")
    return render(request, "pos/category.html", {"categories": categories})

def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        slug = request.POST.get("slug") or slugify(name)
        status = request.POST.get("status", "Active")
        if Category.objects.filter(slug=slug).exists():
            return JsonResponse({"error": "Category already exists"}, status=400)
        category = Category.objects.create(name=name, slug=slug, status=status)
        return JsonResponse({"success": True, "category": {
            "id": category.id,
            "name": category.name,
            "slug": category.slug,
            "status": category.status,
        }})
    return JsonResponse({"error": "Invalid request"}, status=400)

def edit_category(request, id):
    if request.method == "POST":
        try:
            category = Category.objects.get(id=id)
            category.name = request.POST.get("name")
            category.slug = request.POST.get("slug") or slugify(category.name)
            category.status = request.POST.get("status", "Active")
            category.save()
            return JsonResponse({"success": True, "category": {
                "id": category.id,
                "name": category.name,
                "slug": category.slug,
                "status": category.status,
            }})
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_category(request, id):
    if request.method == "POST":
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return JsonResponse({"success": True})
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)


# ----- Manage Stocks -----
example_stocks = []  # Temporary in-memory store

def manage_stocks(request):
    return render(request, "pos/manage_stocks.html", {"stocks": example_stocks})

def add_stock(request):
    if request.method == "POST":
        product = request.POST.get("product")
        category = request.POST.get("category")
        brand = request.POST.get("brand")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        type_ = request.POST.get("type")
        owner = request.POST.get("owner")
        new_id = max([s["id"] for s in example_stocks], default=0) + 1
        stock_item = {
            "id": new_id,
            "product": product,
            "category": category,
            "brand": brand,
            "price": price,
            "stock": stock,
            "type": type_,
            "owner": owner,
        }
        example_stocks.append(stock_item)
        return JsonResponse({"success": True, "stock": stock_item})
    return JsonResponse({"error": "Invalid request"}, status=400)

def edit_stock(request, stock_id):
    if request.method == "POST":
        stock_item = next((s for s in example_stocks if s["id"] == stock_id), None)
        if stock_item:
            stock_item.update({
                "product": request.POST.get("product"),
                "category": request.POST.get("category"),
                "brand": request.POST.get("brand"),
                "price": request.POST.get("price"),
                "stock": request.POST.get("stock"),
                "type": request.POST.get("type"),
                "owner": request.POST.get("owner"),
            })
            return JsonResponse({"success": True, "stock": stock_item})
        return JsonResponse({"error": "Stock not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_stock(request, stock_id):
    if request.method == "POST":
        global example_stocks
        example_stocks = [s for s in example_stocks if s["id"] != stock_id]
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid request"}, status=400)

    # ----- Dashboards -----
def admin_dashboard(request):
    return render(request, "pos/admin_dashboard.html")

def manager_dashboard(request):
    return render(request, "pos/manager_dashboard.html")

def users(request):
    return render(request, "pos/users.html")

    # ----- Roles & Permissions -----
def roles_permissions(request):
    return render(request, "pos/roles_permissions.html")

    # ----- delete_account -----
def delete_account(request):
    # For now, just render the template; later you can add CRUD logic
    return render(request, "pos/delete_account.html")

    #-----reports page-----
    


