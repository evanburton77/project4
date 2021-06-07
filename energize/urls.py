from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('drinks/', views.DrinkList.as_view(), name='drink_list'),
    path('drinks/<int:pk>', views.DrinkDetail.as_view(), name='drink_detail'),
]