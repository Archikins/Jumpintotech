# Generated by Django 3.0.5 on 2020-06-20 12:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_frase'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Pagina HTML'),
        ),
    ]