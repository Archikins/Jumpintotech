# Generated by Django 3.0.5 on 2020-06-17 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JIT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='imageM',
            field=models.ImageField(default='null', upload_to='Proyectos'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='imaget',
            field=models.ImageField(default='null', upload_to='Proyectos'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='image',
            field=models.ImageField(default='null', upload_to='Proyectos'),
        ),
        migrations.AlterField(
            model_name='tipoproyecto',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
