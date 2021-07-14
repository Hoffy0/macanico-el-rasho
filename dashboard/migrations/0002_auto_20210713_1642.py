# Generated by Django 3.2.4 on 2021-07-13 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Marca')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la marca')),
                ('logo', models.CharField(max_length=500, verbose_name='Logo de la marca')),
            ],
        ),
        migrations.AlterModelOptions(
            name='reparaciones',
            options={'ordering': ['Completa']},
        ),
        migrations.RemoveField(
            model_name='reparaciones',
            name='vehiculo',
        ),
        migrations.AddField(
            model_name='reparaciones',
            name='Completa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reparaciones',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dashboard.categoria'),
        ),
        migrations.AddField(
            model_name='reparaciones',
            name='modelo',
            field=models.CharField(default='', max_length=20, verbose_name='Modelo'),
        ),
        migrations.AddField(
            model_name='reparaciones',
            name='patente',
            field=models.CharField(default='', max_length=6, verbose_name='Patente'),
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
        migrations.AddField(
            model_name='reparaciones',
            name='marca',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='dashboard.marca'),
        ),
    ]
