# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 03:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieKu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_movie', models.CharField(max_length=50, verbose_name='Kode Movie')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('kode_identitas', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Kode Identitas')),
                ('nama', models.CharField(max_length=200, verbose_name='Nama')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='movieku',
            name='pengguna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_10.Pengguna'),
        ),
    ]
