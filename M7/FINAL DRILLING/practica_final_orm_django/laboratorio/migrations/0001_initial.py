# Generated by Django 4.0.5 on 2023-08-05 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('f_fabricacion', models.DateField()),
                ('p_costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('p_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('laboratorio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
        ),
    ]
