# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField()),
                ('headline', models.CharField(max_length=100)),
                ('abstract', models.TextField(max_length=100)),
                ('copy', models.TextField(max_length=300)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('bio', models.CharField(max_length=140)),
                ('academic_year', models.IntegerField()),
                ('school', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.SlugField(max_length=32, unique=True)),
            ],
            options={
                'ordering': ('text',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(
                related_name='articles', to='unicorn.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(
                related_name='articles', to='unicorn.Tag'),
        ),
    ]