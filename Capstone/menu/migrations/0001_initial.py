# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('type', models.CharField(default=None, max_length=30)),
            ],
            options={
                'verbose_name': 'Category for Food Type',
                'verbose_name_plural': 'Category for Food Type',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(default=None, max_length=30)),
            ],
            options={
                'verbose_name': 'Menu Management',
                'verbose_name_plural': 'Menu Management',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('date', models.DateField(verbose_name='Published on')),
                ('review', models.TextField(default=None, max_length=200)),
                ('name', models.ForeignKey(default=None, to='menu.FoodItem')),
                ('title', models.ForeignKey(default=None, to='menu.Menu')),
                ('type', models.ForeignKey(default=None, to='menu.FoodType')),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='title',
            field=models.ForeignKey(default=None, to='menu.Menu'),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='type',
            field=models.ForeignKey(default=None, to='menu.FoodType'),
        ),
    ]
