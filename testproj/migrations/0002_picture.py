# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-21 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('testproj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_nr', models.IntegerField(help_text='Just a dummy number')),
            ],
            options={
                'verbose_name': 'picture',
                'verbose_name_plural': 'pictures',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PictureTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('caption', models.CharField(max_length=50)),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='testproj.Picture')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='picturetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]