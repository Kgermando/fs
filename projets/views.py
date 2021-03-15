from django.shortcuts import render

# Create your views here.

def projets(request):

    context = {}
    template_name = 'pages/projets/projets.html'
    return render(request, template_name, context)
