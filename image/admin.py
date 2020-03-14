from django.contrib import admin

# Register your models here

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'status']
    list_filter = ['status']


class ImageAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'category', 'status']
    list_filter = ['category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
