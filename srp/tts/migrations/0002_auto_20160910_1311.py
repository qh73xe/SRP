# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openjtalk',
            name='openJTalk',
            field=models.FilePathField(verbose_name=b'/home/qh73xe/Documents/prod/forODA/SRP/_TOOLS/bin'),
        ),
    ]
