# Generated by Django 4.2.7 on 2023-12-02 22:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='groupe',
            name='category',
            field=models.CharField(choices=[('IT', 'It'), ('fonc', 'Fonctionnel'), ('mgt', 'Management')], default='IT', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupe',
            name='creation',
            field=models.IntegerField(default=2023, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupe',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupe',
            name='page',
            field=models.URLField(blank=True, null=True),
        ),
    ]
