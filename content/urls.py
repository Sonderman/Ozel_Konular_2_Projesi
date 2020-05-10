from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/<slug:slug>', views.contentdetail, name='contentdetail'),
]
