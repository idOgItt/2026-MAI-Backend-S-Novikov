"""JSON-заглушки: JsonResponse и ограничение HTTP-методов."""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def api_profile(request):
    return JsonResponse(
        {
            "stub": True,
            "endpoint": "profile",
            "user_id": getattr(request.user, "id", None) if request.user.is_authenticated else None,
        }
    )


@require_http_methods(["GET"])
def api_products_list(request):
    return JsonResponse(
        {
            "stub": True,
            "endpoint": "products",
            "items": [],
        }
    )


@require_http_methods(["GET"])
def api_product_detail(request, product_id: int):
    return JsonResponse(
        {
            "stub": True,
            "endpoint": "product_detail",
            "id": product_id,
        }
    )


@require_http_methods(["GET"])
def api_categories_list(request):
    return JsonResponse(
        {
            "stub": True,
            "endpoint": "categories",
            "items": [],
        }
    )


@require_http_methods(["GET"])
def api_category_detail(request, category_id: int):
    return JsonResponse(
        {
            "stub": True,
            "endpoint": "category",
            "id": category_id,
        }
    )


@require_http_methods(["POST"])
def api_favorites_add(request):
    return JsonResponse(
        {
            "stub": True,
            "endpoint": "favorites_add",
            "status": "accepted",
        },
        status=201,
    )
