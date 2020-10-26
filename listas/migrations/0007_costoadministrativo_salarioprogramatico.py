# Generated by Django 2.2 on 2020-10-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0006_personasviajan'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoAdministrativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Costo administrativo',
                'verbose_name_plural': 'Costo administrativo',
            },
        ),
        migrations.CreateModel(
            name='SalarioProgramatico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Salario Programatico',
                'verbose_name_plural': 'Salario Programatico',
            },
        ),
    ]