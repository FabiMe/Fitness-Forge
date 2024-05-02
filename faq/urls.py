from django.urls import path
from .views import faq_list, add_faq

urlpatterns = [
    path('', faq_list, name='faq_list'),
    path('add/', add_faq, name='add_faq'),
]