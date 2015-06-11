# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to=b'imgs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
