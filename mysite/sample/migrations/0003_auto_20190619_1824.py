# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-19 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20190619_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.ImageField(blank=True, default='default.png', upload_to=b''),
        ),
    ]