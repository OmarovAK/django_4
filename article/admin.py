from django.contrib import admin
from .models import Article, Scope, Tag


class ScopeInline(admin.TabularInline):
    model = Scope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['published_at', ]
    inlines = [ScopeInline, ]
