from django.urls import path, include
from .  import views

urlpatterns = [
    path('account' , views.show_account, name='account' ),    
    path('logout' , views.sign_out, name='logout' ),    
]