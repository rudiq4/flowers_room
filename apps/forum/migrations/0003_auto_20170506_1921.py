# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='forum.Tag'),
        ),
    ]
