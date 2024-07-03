from django.urls import path

from .views import add_faq, faq_list

urlpatterns = [
    path("", faq_list, name="faq_list"),
    path("add/", add_faq, name="add_faq"),
]
