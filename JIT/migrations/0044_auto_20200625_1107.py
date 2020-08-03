# Generated by Django 3.0.5 on 2020-06-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JIT', '0043_reviews_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='image',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='bussiness',
            field=models.CharField(max_length=100, verbose_name='Empresa'),
        ),
    ]
