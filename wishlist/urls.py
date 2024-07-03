from django.urls import path
from .views import add_to_wishlist, view_wishlist, remove_from_wishlist


urlpatterns = [
    path("wishlist/add/<int:product_id>/", add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/", view_wishlist, name="view_wishlist"),
    path(
        "wishlist/remove/<int:product_id>/",
        remove_from_wishlist,
        name="remove_from_wishlist",
    ),
]
