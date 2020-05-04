from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.index, name='index'),
    path('update/', views.profile_update, name='profile_update'),
    path('password/', views.change_password, name='change_password'),

]
