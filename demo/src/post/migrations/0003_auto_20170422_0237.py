# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-22 02:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170422_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='post_id',
        ),
    ]