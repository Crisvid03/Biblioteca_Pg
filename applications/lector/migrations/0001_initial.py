# Generated by Django 5.0.7 on 2024-07-13 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('country', models.CharField(max_length=50, verbose_name='Nacionalidad')),
                ('old', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(verbose_name='fecha de salida')),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('entregado', models.BooleanField()),
                ('lector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lector.lector')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.libro')),
            ],
        ),
    ]