from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from home.models import UserProfile, UserProfileForm
from photo.models import Category, Comment
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    current_user = request.user
    category = Category.objects.all()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category, 'profile': profile}
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
        return render(request, 'Pages/User/update_profile.html', context)


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
def delete_comment(request,id):
    current_user=request.user
    Comment.objects.get(id=id,user_id=current_user.id).delete()
    messages.success(request, "Your Comment is successfully deleted")
    return  HttpResponseRedirect('/user/comments')

