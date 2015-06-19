# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OCR', '0008_auto_20150612_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docupload',
            name='uploaded_doc',
            field=models.ImageField(upload_to=b'uploads/'),
            preserve_default=True,
        ),
    ]
