# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-19 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_auto_20190619_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='image/'),
        ),
    ]
