# Generated by Django 3.0.5 on 2020-06-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JIT', '0037_tiponoticia_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Orden de aparición'),
        ),
    ]
