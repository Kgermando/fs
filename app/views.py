from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.contrib import messages # for message
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings

from app.models import Product, ContactForm, Like
# Create your views here.
def index(request):
    query = request.GET.get('q', '')
    #The empty string handles an empty "request"
    if query:
            queryset = (
                Q(title__icontains=query) | 
                Q(resume__icontains=query) | 
                Q(description__icontains=query) | 
                Q(prix__icontains=query) |
                Q(rate__icontains=query) |
                Q(categorie__icontains=query) |
                Q(Mot_cles__icontains=query) |
                Q(themes__icontains=query)
            )
            results = Product.objects.filter(queryset).distinct()
    else:
        results = []

    product_list = Product.objects.all().order_by('-created')[:12]
    product_slide = Product.objects.all()

    if 'add_cart' in request.COOKIES:
        add_cart = request.COOKIES['add_cart']
        counter = add_cart.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    context = {
        'results': results,
        'query': query,
        'product_list': product_list,
        'product_slide': product_slide,
        'product_count_in_cart':product_count_in_cart
    }
    template_name = 'pages/app/index.html'
    return render(request, template_name, context)


def view(request, slug):
    """
        Search detail
    """
    if 'add_cart' in request.COOKIES:
        add_cart = request.COOKIES['add_cart']
        counter = add_cart.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    product = get_object_or_404(Product, slug=slug)
    product_list = Product.objects.all().order_by('-created')[:3]
    product.page_views = product.page_views + 1
    product.save()

    # Favoris fr owner user
    id = product.id
    if request.method == 'POST':
        user = request.user
        like = request.POST.get(['like'])
        product = request.id
        liked = Like(user=user, like=like, product=product)
        liked.save()
    # else:

    # is_liked = Like.objects.filter(product=id).filter(user=request.user)
    # if is_liked:
    #     return True
    # else:
    #     return False


    context = {
        'product': product,
        'product_list': product_list,
        'product_count_in_cart':product_count_in_cart
    }
    template_name = 'pages/app/view.html'
    return render(request, template_name, context)



# def like_book(request, bookid):
#     current_book = Book.objects.get(id=bookid)
#     current_user = User.objects.get(id=request.session['userid'])
#     current_book.users_who_like.add(current_user)
#     return redirect('/books/'+str(bookid))


# def unlike_book(request, bookid):
#     current_book = Book.objects.get(id=bookid)
#     current_user = User.objects.get(id=request.session['userid'])
#     current_book.users_who_like.remove(current_user)
#     return redirect('/books/'+str(bookid))



def contact(request):

    if 'add_cart' in request.COOKIES:
        add_cart = request.COOKIES['add_cart']
        counter = add_cart.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    if  request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact_us = ContactForm(name=name,email=email,message=message)
        contact_us.save()
        messages.success(request,'! Nous avons réçu votre message')
        # request.message = "The story was not found. It might have  been deleted by the user."
        return redirect('app:contact')
    context = {
        'product_count_in_cart':product_count_in_cart
    }
    template_name = 'pages/app/contact.html'
    return render(request, template_name, context)


# def contactus_view(request):
#     sub = forms.ContactusForm()
#     if request.method == 'POST':
#         sub = forms.ContactusForm(request.POST)
#         if sub.is_valid():
#             email = sub.cleaned_data['Email']
#             name=sub.cleaned_data['Name']
#             message = sub.cleaned_data['Message']
#             send_mail(str(name)+' || '+str(email),message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
#             return render(request, 'ecom/contactussuccess.html')
#     return render(request, 'ecom/contactus.html', {'form':sub})

