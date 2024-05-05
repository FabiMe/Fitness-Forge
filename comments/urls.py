from django.urls import path
from products.views import product_detail
from .views import delete_comment


urlpatterns = [
    path(
        'product/<int:pk>/',
        product_detail,
        name='product_detail'
    ),
    path(
        'delete_comment/<int:comment_id>/',
        delete_comment,
        name='delete_comment'
    ),
]
