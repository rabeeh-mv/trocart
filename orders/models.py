from django.db import models
from customers.models import customer
from products.models import Product
# Create your models here.

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE=0
    ORDER_CUNFORMED=1
    ORDER_REJECTES=2
    ORDER_PROCESSED=3
    ORDER_DELIVERD=4
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERD,"ORDER_DELIVERD"),
                   (ORDER_REJECTES,"ORDER_REJECTES")
                   )
    
    oder_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner =models.ForeignKey(customer, on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class OrderItems(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner= models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')