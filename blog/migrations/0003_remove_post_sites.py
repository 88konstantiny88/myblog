# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_sites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sites',
        ),
    ]