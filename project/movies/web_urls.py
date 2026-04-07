from django.urls import path

from movies import web_views

urlpatterns = [
    path("", web_views.web_home, name="web_home"),
    path("profile/", web_views.web_profile, name="web_profile"),
    path("movies/", web_views.web_products_feed, name="web_movies_feed"),
    path("movies/<int:product_id>/", web_views.web_product_detail, name="web_movie_detail"),
    path("categories/<int:category_id>/", web_views.web_category, name="web_category"),
]
