from django.urls import path

from movies import api_views

urlpatterns = [
    path("profile/", api_views.api_profile, name="api_profile"),
    path("products/", api_views.api_products_list, name="api_products_list"),
    path("products/<int:product_id>/", api_views.api_product_detail, name="api_product_detail"),
    path("categories/", api_views.api_categories_list, name="api_categories_list"),
    path("categories/<int:category_id>/", api_views.api_category_detail, name="api_category_detail"),
    path("favorites/", api_views.api_favorites_add, name="api_favorites_add"),
]
