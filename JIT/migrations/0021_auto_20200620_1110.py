# Generated by Django 3.0.5 on 2020-06-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JIT', '0020_auto_20200620_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='app',
            field=models.BooleanField(default=False, verbose_name='Marcar SOLO si es una app'),
        ),
    ]
