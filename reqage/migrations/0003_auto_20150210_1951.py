# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reqage', '0002_docthing_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lex',
            name='id',
        ),
        migrations.AddField(
            model_name='lex',
            name='docthing',
            field=models.OneToOneField(primary_key=True, default='', serialize=False, to='reqage.DocThing'),
            preserve_default=False,
        ),
    ]
