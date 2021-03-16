from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

from app.models import Product, Like

@login_required(login_url='/accounts/login/')
def like(request,id):
    if request.is_ajax:
        if request.method == 'POST':
            product=Product.objects.get(id= id)
            like=Like.objects.filter(product=product).filter(user=request.user)
            if like:
                like.delete()
                count=Like.objects.filter(product=product).count()
                truth='True'
                is_liked='Like'
            else:
                like=Like()
                like.user=request.user
                like.product=product
                like.like=True
                like.save()
                if(like.product.user.id is not request.user.id):
                    set_notification(like.product.user, request.user.first_name+' '+request.user.last_name +' liked your story.',0,'route("storydetail/'+str(post.id)+'")')
                count=Like.objects.filter(product=product).count()
                truth='False'
                is_liked='Liked'
            return JsonResponse({'count':count,'truth':truth,'is_liked':is_liked})

def get_notification(request):
    notifications=get_last_ten(request.user.id)
    context = {"notifications":notifications}
    template_name = "pages/notifications/notification.html"
    return render(request, template_name, context)
