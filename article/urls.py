from django.urls import path
from .views import article_view, list_pages_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articles'
urlpatterns = [
    path('article/', article_view, name='article_view'),
    path('', list_pages_view, name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
