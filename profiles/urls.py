from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update')
    ,
]
