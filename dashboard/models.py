from django.db import models
from django.contrib.auth.models import User
# Create your models here.
category=(
    ('stationary','stationary'),
    ('electronics','electronics'),
    ('non-technical','non-technical'),
)
class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=category,null=True)
    quantity=models.PositiveIntegerField(null=True)
    about=models.CharField(max_length=300,null=True)

    class Meta:
        verbose_name_plural='Product'
    
    def __str__(self) -> str:
        return f'{self.name}-{self.quantity}'


class Issued_Items(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User,models.CASCADE,null=True)
    issueditem_quantity=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Issued_Items'

    def __str__(self) -> str:
        return f'{self.product} issued to {self.staff}'

