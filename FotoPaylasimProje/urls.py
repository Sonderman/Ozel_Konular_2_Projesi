
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views

"""
Burası sitemizin Routing kısmının ayarlandığı yer
"""
urlpatterns = [
    path('', include('home.urls')),
    path('photo/', include('photo.urls')),
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('category/<int:id>/<slug:slug>/', views.category_view, name='category_view'),
    path('menu/<int:id>/', views.menu, name='menu'),
    path('error/', views.error, name='error'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
