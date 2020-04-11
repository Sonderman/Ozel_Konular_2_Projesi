from django.contrib import admin

# Register your models here

from .models import *


class ImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['category']
    inlines = [ImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Images, ImagesAdmin)
