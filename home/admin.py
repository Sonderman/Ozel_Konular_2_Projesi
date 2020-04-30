from django.contrib import admin

# Register your models here.

from .models import *


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status']
    list_filter = ['status']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'address', 'city', 'country', 'image_tag']


admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
