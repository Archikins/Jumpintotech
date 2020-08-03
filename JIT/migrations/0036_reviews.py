# Generated by Django 3.0.5 on 2020-06-22 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JIT', '0035_metodologiajit'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nombre')),
                ('charge', models.CharField(max_length=200, verbose_name='Cargo')),
                ('description', models.TextField(verbose_name='Review')),
                ('bussiness', models.CharField(max_length=100, verbose_name='Cargo')),
                ('public', models.BooleanField(default=False, verbose_name='¿Público?')),
                ('image', models.FileField(default='null', upload_to='Noticias', verbose_name='Imagen')),
                ('language', models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha modificado')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Reviews',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
