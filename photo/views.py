from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from home.models import UserProfile
from .models import *


# Create your views here.
def index(request):
    return HttpResponse("Image page")


@login_required(login_url='/login')
def addcomment(request, id):
    current_user_profil = UserProfile.objects.get(pk=request.user.id)
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id = current_user.id
            data.userprofil = current_user_profil
            data.photo_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your review Succesfully received, Thank you")
            return HttpResponseRedirect(url)
    messages.warning(request, "Error Occured!!")
    return HttpResponseRedirect(url)
