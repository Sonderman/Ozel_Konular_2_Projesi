from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from photo.models import *
from .models import *


def index(request):
    #data = Photo.objects.all().order_by('-id')[4]
    # data = Photo.objects.all().order_by('?')[4]
    #photo = Photo.objects.filter(category_id=id
    setting = Setting.objects.get(pk=1)
    sliderdata = Photo.objects.all()[:4]
    category = Category.objects.all()
    photos = Photo.objects.all()[:10]
    context = {'setting': setting, 'sliderdata': sliderdata, 'category': category, 'photos': photos}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been succesfully sent, Thank you")
            return HttpResponseRedirect('/contact')
    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting, 'form': form}
    return render(request, 'Pages/contactPage.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'Pages/aboutUsPage.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'Pages/referencesPage.html', context)


def photo_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    photo = Photo.objects.filter(category_id=id)
    context = {'setting': setting, 'photo': photo}
    return render(request, 'Pages/photoDetail.html', context)
