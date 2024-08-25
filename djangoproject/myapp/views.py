from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm
from .models import Item, Menu


# Create your views here.
def index(request):
    return render(request,'index.html')

def all_item(request):
    items = Item.objects.all()
    return render(request,'all.html',{"items":items})

def breakfast(request):
    breakfast = get_object_or_404(Menu, menu_name="Breakfast")
    print(breakfast)
    items = Item.objects.filter(menu=breakfast)
    return render(request,'all.html',{"items":items})

def price(request):
    items = Item.objects.filter(price__gte=2000, price__lte=5000)
    return render(request,'all.html',{"items":items})

def calories(request):
    items = Item.objects.filter(calories__lte=20).order_by('item_name')
    return render(request,'all.html',{"items":items})

def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all')  # Replace 'success_url' with the URL to redirect after successful form submission
    else:
        form = ItemForm()
    return render(request, 'create.html', {'form': form})

def delete(request, id):
    Item.objects.get(id=id).delete()
    return HttpResponseRedirect('/all')

def update(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all') # Redirect to home page or any other appropriate URL after update
    else:
        form = ItemForm(instance=item)
    return render(request, 'update.html', {'form': form})