from django.shortcuts import render

# Create your views here.

def projets(request):

    if 'add_cart' in request.COOKIES:
        add_cart = request.COOKIES['add_cart']
        counter = add_cart.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0
        
    context = {
        'product_count_in_cart':product_count_in_cart
    }
    template_name = 'pages/projets/projets.html'
    return render(request, template_name, context)
