from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from content.models import Menu
from home.models import UserProfile, UserProfileForm, Setting
from photo.models import Category, Comment, Photo, PhotoForm
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    current_user = request.user
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category, 'setting': setting, 'profile': profile}
    return render(request, 'Pages/User/profile_main.html', context)


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your account has been succesfully updated.")
            return redirect('/user/profile')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'Pages/User/update_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been succesfully updated.")
            return redirect('change_password')
        else:
            messages.warning(request, "Error!!.<br>" + str(form.errors))
            return redirect('change_password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {
            'category': category,
            'form': form,
        }
        return render(request, 'Pages/User/change_password.html', context)


@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'comments': comment,
    }
    return render(request, 'Pages/User/commentsPage.html', context)


@login_required(login_url='/login')
def delete_comment(request, id):
    current_user = request.user
    Comment.objects.get(id=id, user_id=current_user.id).delete()
    messages.success(request, "Your Comment is successfully deleted")
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def addphoto(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Photo()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.category_id = form.cleaned_data['category'].id
            data.save()
            messages.success(request, "Photo succesfully added")
            return HttpResponseRedirect("/user/photos")
        else:
            messages.warning(request, "Error:" + str(form.errors))
            return HttpResponseRedirect("/user/addphoto")
    else:
        category = Category.objects.all()
        form = PhotoForm()
        context = {
            'category': category,
            'form': form,
        }
        return render(request, 'Pages/User/add_photoPage.html', context)


@login_required(login_url='/login')
def photos(request):
    category = Category.objects.all()
    menu = Menu.objects.all()
    photo = Photo.objects.filter(user_id=request.user.id, status='True')
    context = {
        'category': category,
        'photos': photo,
    }
    return render(request, 'Pages/User/photosPage.html', context)


@login_required(login_url='/login')
def photoedit(request, id):
    photo = Photo.objects.get(id=id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.status = 'False'
            photo.save()
            messages.success(request, "Photo succesfully Edited")
            return HttpResponseRedirect("/user/photos")
        else:
            messages.warning(request, "Error:" + str(form.errors))
            return HttpResponseRedirect("/user/photoedit/" + str(id))
    else:
        category = Category.objects.all()
        form = PhotoForm(instance=photo)
        context = {
            'category': category,
            'form': form,
        }
        return render(request, 'Pages/User/add_photoPage.html', context)


@login_required(login_url='/login')
def photodelete(request, id):
    Photo.objects.filter(id=id, user_id=request.user.id).delete()
    messages.success(request, "Photo deleted..")
    return HttpResponseRedirect('/user/photos')
