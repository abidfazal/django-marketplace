from django import forms 

from .models import Item

class NewItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('catagory','name','description','price','image',)

