# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reqage', '0004_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='associated',
            field=models.ManyToManyField(related_name='associated_rel_+', to='reqage.Requirement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verification',
            name='associated',
            field=models.ManyToManyField(related_name='associated_rel_+', to='reqage.Verification'),
            preserve_default=True,
        ),
    ]
