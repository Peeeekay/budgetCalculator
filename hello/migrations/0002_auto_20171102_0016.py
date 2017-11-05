# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.IntegerField()),
                ('month', models.CharField(max_length=15)),
                ('biWeekly', models.IntegerField()),
                ('currDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
