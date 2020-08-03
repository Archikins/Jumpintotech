# Generated by Django 3.0.5 on 2020-06-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JIT', '0018_auto_20200619_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
        migrations.AddField(
            model_name='paso_filosofia',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
        migrations.AddField(
            model_name='post_blog',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
        migrations.AddField(
            model_name='tiponoticia',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
        migrations.AddField(
            model_name='tipoproyecto',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
        migrations.AddField(
            model_name='tiposervicio',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'English')], default='es', max_length=10, verbose_name='Lenguaje'),
        ),
    ]
