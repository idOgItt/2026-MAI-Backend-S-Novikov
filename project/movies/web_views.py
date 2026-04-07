"""Простые HTML-страницы под префиксом /web/."""

from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def web_home(request):
    return render(request, "movies/web/home.html")


@require_http_methods(["GET"])
def web_profile(request):
    return render(request, "movies/web/profile.html")


@require_http_methods(["GET"])
def web_products_feed(request):
    return render(request, "movies/web/feed.html")


@require_http_methods(["GET"])
def web_product_detail(request, product_id: int):
    return render(
        request,
        "movies/web/detail.html",
        {"product_id": product_id},
    )


@require_http_methods(["GET"])
def web_category(request, category_id: int):
    return render(
        request,
        "movies/web/category.html",
        {"category_id": category_id},
    )
