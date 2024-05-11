from django.shortcuts import get_object_or_404, render

from item.models import Item

# Create your views here.
def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(catagory=item.catagory,is_sold=False).exclude(pk=pk)[0:3]
    
    return render(request,'item/detail.html',{'item':item,'related_items':related_items})