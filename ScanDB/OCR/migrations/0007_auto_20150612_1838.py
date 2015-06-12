# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OCR', '0006_remove_docupload_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docupload',
            name='uploaded_doc',
            field=models.ImageField(upload_to=b'update_filename'),
            preserve_default=True,
        ),
    ]
