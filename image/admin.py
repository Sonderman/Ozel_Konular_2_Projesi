from django.contrib import admin

# Register your models here

from .models import *


class ImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'status']
    list_filter = ['status']


class ImageAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'category', 'status']
    list_filter = ['category']
    inlines = [ImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent_image', 'image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Images, ImagesAdmin)
