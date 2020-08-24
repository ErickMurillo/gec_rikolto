# Generated by Django 3.0.9 on 2020-08-24 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('anio_inicio', models.DateField()),
                ('anio_fin', models.DateField()),
                ('aliados', models.ManyToManyField(to='listas.Aliados')),
                ('financiadores', models.ManyToManyField(to='listas.Finaciadores')),
                ('org_implementador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listas.OrgImplementador', verbose_name='Oganización implementador')),
                ('org_socias', models.ManyToManyField(to='listas.OrgSocias', verbose_name='Organizaciones socias clave por país')),
                ('paises', models.ManyToManyField(to='listas.Pais', verbose_name='Países metas')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]
