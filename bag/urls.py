from django.urls import path
from . import views
from .views import remove_from_bag

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('bag/remove/<str:customization_key>/', remove_from_bag, name='remove_from_bag'),
    path('save_customization/', views.save_customization, name='save_customization'),
]