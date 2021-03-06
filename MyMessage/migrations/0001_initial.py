# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=200)),
                ('receiver', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('unread', models.BooleanField(default=True)),
                ('from_ta', models.BooleanField(default=False)),
                ('from_student', models.BooleanField(default=False)),
                ('from_admin', models.BooleanField(default=False)),
                ('from_parents', models.BooleanField(default=False)),
                ('first_message', models.BooleanField(default=True)),
                ('reply_to', models.IntegerField(blank=True)),
            ],
        ),
    ]
