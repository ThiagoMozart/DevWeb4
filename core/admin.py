from django.contrib import admin

from .models import Image, News, History, Chapter


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('name', 'path')
    search_fields = ('name',)
    list_display = ('name', 'path')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    search_fields = ('title',)
    list_display = ('title', 'description')


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    fields = ('battle_name', 'image', 'description', 'curiosity')
    search_fields = ('battle name',)
    list_display = ('battle_name', 'description', 'curiosity', 'image')


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'catchphrase')
    search_fields = ('name',)
    list_display = ('name', 'catchphrase', 'image')
