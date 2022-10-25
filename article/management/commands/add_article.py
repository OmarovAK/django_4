import json
import os
from django.core.management.base import BaseCommand
from article.models import Article


class Command(BaseCommand):

    def handle(self, *args, **options):
        file = os.path.join(os.getcwd(), 'article.json')
        with open(file, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        list_id_from_article_table = [i.id for i in Article.objects.all()]
        for i in data:
            if i['pk'] not in list_id_from_article_table:
                Article.objects.create(id=i['pk'], title=i['fields']['title'], text=i['fields']['text'],
                                       published_at=i['fields']['published_at'], image=i['fields']['image'])


