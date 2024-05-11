from django.shortcuts import render
from item.models import Catagory,Item

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)
    catagories = Catagory.objects.all()
    context  = {
        'items':items,
        'catagories':catagories
    }
    return render(request, 'core/index.html',context)


def contact(request):
    return render(request,'core/contact.html')[0:6]

