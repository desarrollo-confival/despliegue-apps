# Generated by Django 2.2.6 on 2020-01-30 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juridicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='juridicos',
            options={'managed': True, 'ordering': ['codigo'], 'verbose_name': 'Jurídico', 'verbose_name_plural': 'Jurídicos'},
        ),
    ]