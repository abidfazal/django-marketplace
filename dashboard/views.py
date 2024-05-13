from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from item.models import Item
# Create your views here.

@login_required

def index1(request):
    
    items = Item.objects.filter(create_by=request.user)
    
    return render(request,'dashboard/index.html',{'items':items})



    
