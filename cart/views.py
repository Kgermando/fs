from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse

from app.models import Product
from cart.models import Cart
# Create your views here.

@login_required
def cart(request, pk):
    user = User.objects.get(pk=pk)
    cart = Cart.objects.filter(user=user)
    cart_n = Cart.objects.filter(user=user).count()
    total = 0
    paginator = Paginator(cart, 10)
    page = request.GET.get('page')
    try:
        cart = paginator.page(page)
    except PageNotAnInteger:
        cart = paginator.page(1)
    except EmptyPage:
        cart = paginator.page(paginator.num_pages)

    for c in cart:
        total = total + c.products.prix

    context = {
        'user': user, 
        'cart': cart,
        'cart_n': cart_n,
        'total':total,
    }
    template_name = 'pages/cart/cart.html'

    return render(request, template_name, context)

@login_required
def delete_cart(request, pk):
    user = request.user
    cart = Cart.objects.filter(user=user)


    if request.method == 'POST':
        # pk = int(request.POST.get('product'))
        prod = int(request.POST.get('prod'))

        product = Product.objects.get(pk=prod)
        for i in cart:
            if i.products == product:
                product = Product.objects.filter(pk=pk)
                cart = Cart.objects.filter(user=user, products__in=product)
                cart.delete()
            return redirect('cart:cart', user.pk)



@login_required
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    cart = Cart.objects.filter(user=user)

        # for cart counter, fetching products ids added by customer from cookies
    if 'add_cart' in request.COOKIES:
        add_cart = request.COOKIES['add_cart']
        counter=add_cart.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=1

    if request.method == 'POST':
        if 'add_cart' in request.POST:
            for i in cart :
                if i.products == product:
                    product = Product.objects.filter(pk=pk)
                    Cart.objects.filter(user=user, products__in=product)
                    messages.success(request,'Enregistrement du panier terminé')
                    return redirect('cart:cart', user.pk)

            Cart.objects.create(user=user, products=product)
            messages.success(request, '! Ajouté au panier')
            return redirect('cart:cart', user.pk)
    
    response = render(request, 'pages/cart/cart.html', {'product_count_in_cart':product_count_in_cart})

    # adding product id to cookies
    if 'add_cart' in request.COOKIES:
        add_cart = request.COOKIES['add_cart']
        if add_cart=="":
            add_cart=str(pk)
        else:
            add_cart=add_cart+"|"+str(pk)
        response.set_cookie('add_cart', add_cart)
    else:
        response.set_cookie('add_cart', user.pk)

    return response

