# Generated by Django 4.1.2 on 2022-10-25 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_tag_options_alter_scope_article_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
