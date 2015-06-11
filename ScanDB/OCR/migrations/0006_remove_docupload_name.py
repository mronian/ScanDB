# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OCR', '0005_docupload_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docupload',
            name='name',
        ),
    ]
