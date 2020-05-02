from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from home.models import UserProfile


def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'profile': profile}
    return render(request, 'Pages/User/profile_main.html', context)
