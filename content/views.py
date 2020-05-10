from django.http import *
from django.shortcuts import render

# Create your views here.
from content.models import Menu, Content, CImages
from photo.models import Category, Comment


def index(request):
    return HttpResponse("adsaa")


def contentdetail(request, id, slug):
    try:
        category = Category.objects.all()
        menu = Menu.objects.all()
        content = Content.objects.get(pk=id)
        images = CImages.objects.filter(content_id=id)
        # comments = Comment.objects.filter(photo_id=id, status="True")
        context = {'category': category, 'menu': menu, 'content': content, 'images': images}
        return render(request, 'Pages/content_detail.html', context)
    except:
        return HttpResponseRedirect("/error")
