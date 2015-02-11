# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainreq', '0003_remove_lex_modeltype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('lex_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='trainreq.Lex')),
            ],
            options={
                'abstract': False,
            },
            bases=('trainreq.lex',),
        ),
    ]
