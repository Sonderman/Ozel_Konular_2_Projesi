from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.index, name='index'),
    path('update/', views.profile_update, name='profile_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.delete_comment, name='delete_comment'),
    path('addphoto/', views.addphoto, name='addphoto'),
    path('photos/', views.photos, name='photos'),
    path('photoedit/<int:id>', views.photoedit, name='photoedit'),
    path('photodelete/<int:id>', views.photodelete, name='photodelete'),
]
