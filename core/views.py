from django.contrib.auth import logout
from django.shortcuts import render, redirect
from item.models import Categories, Item
from .forms import SigupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)
    categories = Categories.objects.all()

    # To be able to use them in the template, we need to create a context
    
    return render(request, 'core/index.html',{
        'categories' :categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SigupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SigupForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(request, "core:logout")



