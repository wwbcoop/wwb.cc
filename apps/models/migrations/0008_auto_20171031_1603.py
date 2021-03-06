# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_image_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='related',
            field=models.ManyToManyField(blank=True, help_text='Otros proyectos relacionados con éste.', to='models.Project', verbose_name='Proyectos relacionados'),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('PL', 'Plataformas digitales'), ('HA', 'Prototipado de hardware'), ('IN', 'Instalaciones interactivas'), ('CU', 'Gestión y producción cultural'), ('DI', 'Diseño'), ('TA', 'Talleres y presentaciones')], default='DI', help_text='Categoría del proyecto', max_length=128, verbose_name='Categoría'),
        ),
    ]
