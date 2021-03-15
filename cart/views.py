from django.shortcuts import render

# Create your views here.

def cart(request):

    context = {}
    template_name = 'pages/cart/cart.html'
    return render(request, template_name, context)

