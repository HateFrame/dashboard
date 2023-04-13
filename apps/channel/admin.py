from django.contrib import admin
from .models import Channel, Post


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'channel', 'name', 'content')
