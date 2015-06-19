# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OCR', '0009_auto_20150617_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docupload',
            name='uploaded_doc',
            field=models.ImageField(upload_to=b'uploads/o'),
            preserve_default=True,
        ),
    ]
