# Generated by Django 2.1.2 on 2018-11-01 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantagetopic',
            name='active',
            field=models.BooleanField(blank=True, verbose_name='Seção ativa?'),
        ),
    ]
