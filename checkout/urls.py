from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    # Initiate the checkout process
    path("", views.checkout, name="checkout"),
    # Post-checkout success page
    path(
        "checkout_success/<order_number>",
        views.checkout_success,
        name="checkout_success",
    ),
    # Endpoint for caching checkout data
    path("cache_checkout_data/", views.cache_checkout_data, name="cache_checkout_data"),
    # Webhook endpoint for external notifications
    path("wh/", webhook, name="webhook"),
]
