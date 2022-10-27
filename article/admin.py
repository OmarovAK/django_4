from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Scope, Tag
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if len(form.cleaned_data) > 0:
                if form.cleaned_data['is_main']:
                    count = count + 1
        if count != 1:
            raise ValidationError('Выберите один раздел')
        return super().clean()






class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['published_at', ]
    inlines = [ScopeInline, ]
