from django.urls import path
from . import views

urlpatterns = [
    # Index & Home
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),

    # Category URLs
    path("category/", views.category, name="category"),
    path("category/add/", views.add_category, name="add_category"),
    path("category/edit/<int:id>/", views.edit_category, name="edit_category"),
    path("category/delete/<int:id>/", views.delete_category, name="delete_category"),

    # Products URLs
    path("products/", views.products, name="products"),
    path("products/add/", views.add_product, name="add_product"),
    path("products/<int:product_id>/", views.product_details, name="product_details"),
    path("products/edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("products/delete/<int:product_id>/", views.delete_product, name="delete_product"),

    # Units URLs
    path("units/", views.units, name="units"),
    path("units/add/", views.add_unit, name="add_unit"),
    path("units/edit/<int:unit_id>/", views.edit_unit, name="edit_unit"),
    path("units/delete/<int:unit_id>/", views.delete_unit, name="delete_unit"),

    # Manage Stocks URLs
    path("manage-stocks/", views.manage_stocks, name="manage_stocks"),
    path("manage-stocks/add/", views.add_stock, name="add_stock"),
    path("manage-stocks/edit/<int:stock_id>/", views.edit_stock, name="edit_stock"),
    path("manage-stocks/delete/<int:stock_id>/", views.delete_stock, name="delete_stock"),

    # Other Pages
    path("sales/", views.sales, name="sales"),
    path("report/", views.report, name="report"),

    # Auth Pages
    path("signin/", views.signin, name="signin"),

    # Dashboard Pages
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("manager-dashboard/", views.manager_dashboard, name="manager_dashboard"),

    #Users page
    path("users/", views.users, name="users"),

    # Roles & Permissions page
path("roles-permissions/", views.roles_permissions, name="roles_permissions"),

#Delete account page
path("delete-account/", views.delete_account, name="delete_account"),

#reports page



]
