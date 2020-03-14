from django.contrib import admin

# Register your models here

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'status']
    list_filter = ['status']


admin.site.register(Category, CategoryAdmin)
