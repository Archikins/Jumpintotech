# Generated by Django 3.0.5 on 2020-06-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JIT', '0047_auto_20200626_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Orden de aparición'),
        ),
    ]
