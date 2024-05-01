from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),  # Initiate the checkout process
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),  # Post-checkout success page
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),  # Endpoint for caching checkout data
    path('wh/', webhook, name='webhook'),  # Webhook endpoint for external notifications
]