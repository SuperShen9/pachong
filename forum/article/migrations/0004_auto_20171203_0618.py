# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20171127_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block', verbose_name='板块索引'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=10000, verbose_name='文章内容'),
        ),
    ]
