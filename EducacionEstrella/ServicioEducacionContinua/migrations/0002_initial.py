# Generated by Django 4.0.3 on 2022-05-14 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ServicioEducacionContinua', '0001_initial'),
        ('SucursalAcompañamiento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicioeducacioncontinua',
            name='sucursal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='SucursalAcompañamiento.sucursalacompañamiento'),
        ),
    ]