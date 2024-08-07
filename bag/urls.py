from django.urls import path

from . import views

urlpatterns = [
    path("", views.view_bag, name="view_bag"),
    path("add/<item_id>/", views.add_to_bag, name="add_to_bag"),
    path("adjust/<item_id>/", views.adjust_bag, name="adjust_bag"),
    path("remove/<str:key>/", views.remove_from_bag, name="remove_from_bag"),
    path(
        "save_customization/",  # Notice the indentation here
        views.save_customization,
        name="save_customization",
    ),
]
