from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from item.models import Item
from .forms import NewItemForm

# Create your views here.
def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(catagory=item.catagory,is_sold=False).exclude(pk=pk)[0:3]
    
    return render(request,'item/detail.html',{'item':item,'related_items':related_items})

@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            
            item.create_by  = request.user
            item.save()
            
            return redirect('item:detail',pk=item.id)
            
            
    else:
        form = NewItemForm()
    
    return render(request,'item/form.html',{'form':form,'title':'new item'})


@login_required

def delete(request,pk):
    
    item = get_object_or_404(Item,pk=pk,create_by=request.user)
    item.delete()
    
    return redirect('core:index')