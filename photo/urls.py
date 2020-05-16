from django.urls import path

from . import views

urlpatterns = [
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('gallery/<int:id>', views.gallery),
    path('galleryadd/<int:id>', views.galleryadd),
    path('gallerydelete/<int:id>', views.gallerydelete),
]
