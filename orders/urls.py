from django.urls import path, include
from .  import views

urlpatterns = [
    path('cart' , views.show_cart, name='cart' ),    
]