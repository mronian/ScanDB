# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('OCR', '0004_auto_20150611_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='docupload',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 6, 11, 15, 27, 20, 857985, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
