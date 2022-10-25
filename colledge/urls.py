from django.urls import path
from .views import index_view


app_name = 'migrate_app'
urlpatterns = [

    path('', index_view, name='list_student'),
]