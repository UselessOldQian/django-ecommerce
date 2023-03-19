from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ecommerce-home'),
    path('shopping_cart/', views.shopping_cart, name='ecommerce-shopping_cart'),
    path('cart/add/<str:item_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<str:item_name>/', views.remove_from_cart, name='remove_from_cart')
]
