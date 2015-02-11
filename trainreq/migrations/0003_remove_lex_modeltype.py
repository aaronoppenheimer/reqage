# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainreq', '0002_auto_20150206_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lex',
            name='modeltype',
        ),
    ]
