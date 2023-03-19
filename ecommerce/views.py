from django.shortcuts import render, get_object_or_404
from . models import Item, CartItem
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'eCommerce/home.html', context)


def shopping_cart(request):
    context = {
        'items': CartItem.objects.all(),
        'is_cart': True
    }
    return render(request, 'eCommerce/shopping_cart.html', context)


@login_required
def add_to_cart(request, item_name):
    item = get_object_or_404(Item, name=item_name)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    context = {
        'items': CartItem.objects.all(),
        'is_cart': True
    }

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return render(request, 'eCommerce/shopping_cart.html', context)


@login_required
def remove_from_cart(request, item_name):
    item = get_object_or_404(Item, name=item_name)
    cart_item = CartItem.objects.get(user=request.user, item=item)
    context = {
        'items': CartItem.objects.all(),
        'is_cart': True
    }

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return render(request, 'eCommerce/shopping_cart.html', context)