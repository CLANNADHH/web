# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-22 08:50
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180922_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='文章内容'),
        ),
    ]
