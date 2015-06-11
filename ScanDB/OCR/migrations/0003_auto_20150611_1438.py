# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OCR', '0002_auto_20150611_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docupload',
            name='img',
            field=models.ImageField(upload_to=b'uploads'),
            preserve_default=True,
        ),
    ]
