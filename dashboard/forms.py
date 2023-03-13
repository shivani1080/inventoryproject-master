from django import forms
from .models import Product,Issued_Items
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','quantity','about']

class orderform(forms.ModelForm):
    class Meta:
        model=Issued_Items
        fields=['product','issueditem_quantity']