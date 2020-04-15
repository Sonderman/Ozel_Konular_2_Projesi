from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('references', views.references, name='references'),
    path('photo/<int:id>/<slug:slug>', views.photo_detail, name='photoDetail'),
]
