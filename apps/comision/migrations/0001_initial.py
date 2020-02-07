# Generated by Django 2.2.6 on 2020-01-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comisiones',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('tipo', models.CharField(blank=True, max_length=15, null=True, verbose_name='Tipo de Comision')),
                ('descripcion', models.CharField(blank=True, max_length=20, null=True, verbose_name='Descripción')),
                ('valor', models.FloatField(blank=True, null=True, verbose_name='Valor Comsión')),
            ],
            options={
                'verbose_name': 'Comision del Asesor',
                'verbose_name_plural': 'Comisiones de los Asesores',
                'db_table': 'comisiones',
                'managed': False,
            },
        ),
    ]
