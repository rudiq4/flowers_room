# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 20:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Назва')),
                ('image', models.ImageField(upload_to='albums/', verbose_name='Головне зображення')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Опис')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='gallary.Album')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='Завантажено')),
            ],
        ),
    ]
