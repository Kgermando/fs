from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required


from categorie.models import Category, MotCles, Theme
from app.models import Product

# Create your views here.
def categorie(request, product_slug=None):
    product_promos = Product.objects.filter(promos=True)
    category = None
    category_list = Category.objects.all()
    products = Product.objects.all()

    if product_slug:
        category = get_object_or_404(Category, slug=product_slug)
        products = products.filter(categorie=category)

    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        products_list = paginator.page(page)
    except PageNotAnInteger:
        products_list = paginator.page(1)
    except EmptyPage:
        products_list = paginator.page(paginator.num_pages)

    if 'add_cart' in request.COOKIES:
        add_cart = request.COOKIES['add_cart']
        counter = add_cart.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    context = {
        'category': category,
        'category_list': category_list,
        'products_list': products_list,
        'product_promos': product_promos,
        'product_count_in_cart':product_count_in_cart
    }
    template_name = 'pages/categorie/categorie.html'
    return render(request, template_name, context)


# def motcle_view(request, motcle_slug=None):
#     product_promos = Product.objects.filter(promos=True)
#     motcle = None
#     product_list = Product.objects.all()
#     motcle_list = MotCles.objects.all()
#     if motcle_slug:
#         motcle = get_object_or_404(MotCles, slug=motcle_slug)
#         products = product_list.filter(Mot_cles=motcle)

#     context = {
#         'motcle': motcle,
#         'motcle_list' : motcle_list,
#         'product_list': product_list,
#         'product_promos': product_promos,
#     }
#     template_name = 'pages/categorie/categorie.html'
#     return render(request, template_name, context)


# def theme_view(request, theme_slug=None):
#     product_promos = Product.objects.filter(promos=True)
#     theme = None
#     product_list = Product.objects.all()
#     Theme_list = Theme.objects.all()
#     if theme_slug:
#         theme = get_object_or_404(Theme, slug=theme_slug)
#         products = product_list.filter(themes=theme)

#     context = {
#         'theme': theme,
#         'Theme_list': Theme_list,
#         'product_list': product_list,
#         'product_promos': product_promos,
#     }
#     template_name = 'pages/categorie/categorie.html'
#     return render(request, template_name, context)

