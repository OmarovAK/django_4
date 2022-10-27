from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='article_id')
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tag_id')
    is_main = models.BooleanField(verbose_name='Основной тег')

    class Meta:
        ordering = ['tag_id']


class Tag(models.Model):
    tag = models.CharField(max_length=256)
    article = models.ManyToManyField(Article, related_name='tag', through='Scope')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag
