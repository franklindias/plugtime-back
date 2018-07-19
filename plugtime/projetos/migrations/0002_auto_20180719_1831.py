# Generated by Django 2.0.7 on 2018-07-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='', max_length=255, verbose_name='Título'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='estimated_time',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Tempo estimado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='time_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Título'),
            preserve_default=False,
        ),
    ]
