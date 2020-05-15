from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from content.models import Menu, Content
from photo.models import *
from .forms import SearchForm, SignUpForm
from .models import *
import json


def index(request):
    # data = Photo.objects.all().order_by('-id')[4]
    # data = Photo.objects.all().order_by('?')[:4]
    # photo = Photo.objects.filter(category_id=id)
    setting = Setting.objects.get(pk=1)
    sliderdata = Photo.objects.all()[:4]
    category = Category.objects.all()
    menu = Menu.objects.all()
    # lastphotos = Content.objects.filter(type='photo').order_by('-id')[:4]
    photos = Photo.objects.filter(status='True')[:10]
    context = {'setting': setting, 'sliderdata': sliderdata, 'category': category, 'photos': photos, 'menu': menu}
    return render(request, 'index.html', context)


def category_view(request, id, slug):
    category = Category.objects.all()
    photos = Photo.objects.filter(category_id=id)
    context = {'category': category, 'photos': photos, 'page': 'category_view'}
    return render(request, 'Pages/categoryGallery.html', context)


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
    category = Category.objects.all()
    form = ContactForm()
    context = {'category': category, 'setting': setting, 'form': form}
    return render(request, 'Pages/contactPage.html', context)


def aboutus(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category, 'setting': setting}
    return render(request, 'Pages/aboutUsPage.html', context)


def references(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category, 'setting': setting}
    return render(request, 'Pages/referencesPage.html', context)


def photo_detail(request, id, slug):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    photo = Photo.objects.get(pk=id)
    images = Images.objects.filter(photo=id)
    comments = Comment.objects.filter(photo_id=id, status='True')
    context = {'setting': setting, 'photo': photo, 'imgofphoto': images, 'comments': comments, 'category': category}
    # return HttpResponse(category)
    return render(request, 'Pages/photoDetail.html', context)


def photo_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                photos = Photo.objects.filter(title__icontains=query)
            else:
                photos = Photo.objects.filter(title__icontains=query, category_id=catid)
            context = {'photos': photos, 'category': category, }
            return render(request, 'Pages/photo_search.html', context)
    return HttpResponseRedirect('/')


def search_auto(request):
    print("çalıştı")
    if request.is_ajax():
        q = request.GET.get('term', '')
        photo = Photo.objects.filter(title__icontains=q)
        results = []
        for ph in photo:
            photo_json = {}
            photo_json = ph.title
            results.append(photo_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    category = Category.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Failed!!")
            return HttpResponseRedirect('/login')
    return render(request, 'Pages/login.html', {'category': category})


def signup_view(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("SignUp girdi")

        if form.is_valid():
            print("SignUp Valid Oldu")
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.phone = 0
            user_profile.image = "assets/images/logo.png"
            user_profile.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "SignUp Failed!!<br>" + str(form.errors))
    form = SignUpForm()
    context = {'form': form, 'category': category}
    return render(request, 'Pages/signup.html', context)


def randphoto(request):
    randphotoid = Photo.objects.order_by('?')[:1]
    return HttpResponseRedirect('/photo/' + str(randphotoid[0].id) + '/' + str(randphotoid[0].slug))


def menu(request, id):
    content = Content.objects.get(menu_id=id)
    if content.id:
        link = '/content/' + str(content.id) + '/menu'
        return HttpResponseRedirect(link)
    else:
        messages.warning(request, "Error! Content not found!")
        return HttpResponseRedirect("/")


def error(request):
    return render(request, 'Pages/error_page.html')


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.all().order_by('ordernumber')
    context = {'category': category, 'faq': faq}
    return render(request, 'Pages/faqPage.html', context)
