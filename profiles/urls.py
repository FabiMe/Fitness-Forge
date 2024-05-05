from django.urls import path
from . import views
from .views import account_signup


urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
    ),
    path('signup/', account_signup, name='account_signup'),
]
