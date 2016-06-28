# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tarea_nombre', models.CharField(max_length=120)),
                ('tarea_descripcion', models.TextField()),
                ('tarea_data_inicio', models.DateField(auto_now_add=True)),
                ('concluido', models.BooleanField(verbose_name='Concluido', default=False)),
            ],
        ),
    ]
