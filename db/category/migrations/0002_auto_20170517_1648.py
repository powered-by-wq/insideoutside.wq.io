# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('order', 'name'), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Order'),
        ),
    ]
