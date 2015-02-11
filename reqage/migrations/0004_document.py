# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reqage', '0003_auto_20150210_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('lex_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reqage.Lex')),
            ],
            options={
                'abstract': False,
            },
            bases=('reqage.lex',),
        ),
    ]
