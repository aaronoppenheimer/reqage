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
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('lex_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='trainreq.Lex')),
            ],
            options={
                'abstract': False,
            },
            bases=('trainreq.lex',),
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('lex_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='trainreq.Lex')),
            ],
            options={
                'abstract': False,
            },
            bases=('trainreq.lex',),
        ),
        migrations.AddField(
            model_name='lex',
            name='document',
            field=models.ForeignKey(to='trainreq.Document', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lex',
            name='parent',
            field=models.ManyToManyField(to='trainreq.Lex', blank=True),
            preserve_default=True,
        ),
    ]
