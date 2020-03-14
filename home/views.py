from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    unv="Karabuk Universitesi"
    fakulte="Muhendislik F."
    context={'unv':unv,'fakulte':fakulte}
    return render(request,'index.html',context)

