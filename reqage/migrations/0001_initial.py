# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocThing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('content', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('lex_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reqage.Lex')),
            ],
            options={
                'abstract': False,
            },
            bases=('reqage.lex',),
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('lex_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reqage.Lex')),
            ],
            options={
                'abstract': False,
            },
            bases=('reqage.lex',),
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('lex_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reqage.Lex')),
            ],
            options={
                'abstract': False,
            },
            bases=('reqage.lex',),
        ),
    ]
