# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170327_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcopy',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='bookcopy',
            old_name='library_id',
            new_name='library',
        ),
        migrations.RenameField(
            model_name='bookcopy',
            old_name='user_id',
            new_name='user',
        ),
    ]
