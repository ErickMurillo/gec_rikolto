# Generated by Django 3.0.9 on 2020-10-05 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo_indicadores', '0005_auto_20201005_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndEfecto2_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_empresas', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre de Pólitica/Estrategia actualizada')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado_esfuerzo', models.CharField(blank=True, choices=[('No iniciado', 'No iniciado'), ('Iniciado', 'Iniciado'), ('Avanzado', 'Avanzado'), ('Cumplido', 'Cumplido')], max_length=100, null=True, verbose_name='Estado de esfuerzo')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-efecto-2-1/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndEfectos')),
            ],
            options={
                'verbose_name': 'Indicador 2.1',
                'verbose_name_plural': 'Indicador 2.1',
            },
        ),
    ]
