from django.shortcuts import redirect, render
from item.models import Catagory,Item
from .forms import SignUpForm

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
    return render(request,'core/contact.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            print('form submitted')
            return redirect('/login/')
    else:
        print('form not submited')
        form = SignUpForm()
    
    return render(request,'core/signup.html',{'form':form})

