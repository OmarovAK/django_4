# Generated by Django 4.1.2 on 2022-10-25 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной тег')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=256)),
                ('article', models.ManyToManyField(related_name='tag', through='article.Scope', to='article.article')),
            ],
        ),
        migrations.AddField(
            model_name='scope',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.tag'),
        ),
    ]