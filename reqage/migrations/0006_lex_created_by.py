# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reqage', '0005_auto_20150211_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='lex',
            name='created_by',
            field=models.ForeignKey(related_name='lexs', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
