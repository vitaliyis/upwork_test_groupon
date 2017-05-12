# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=128)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
