# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-15 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Gender', models.CharField(choices=[(b'Female', b'Female'), (b'Male', b'Male'), (b'Other', b'Other')], default=b'Male', max_length=9)),
            ],
        ),
    ]
