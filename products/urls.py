from django.urls import path, include
from .  import views

urlpatterns = [
    path('' , views.index, name='home' ),
    path('product/list' , views.list_products ,name='list_product'),
    path('product/detail' , views.detail_products ,name='detail_products'),

]