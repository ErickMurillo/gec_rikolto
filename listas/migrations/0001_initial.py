# Generated by Django 3.0.9 on 2020-08-24 21:08

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aliados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('logo', sorl.thumbnail.fields.ImageField(upload_to='aliados')),
            ],
            options={
                'verbose_name': 'Aliado',
                'verbose_name_plural': 'Aliados',
            },
        ),
        migrations.CreateModel(
            name='Finaciadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('logo', sorl.thumbnail.fields.ImageField(upload_to='finaciadores')),
            ],
            options={
                'verbose_name': 'Finaciador',
                'verbose_name_plural': 'Finaciadores',
            },
        ),
        migrations.CreateModel(
            name='OrgImplementador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('logo', sorl.thumbnail.fields.ImageField(upload_to='organizaciones')),
            ],
            options={
                'verbose_name': 'Oganización implementador',
                'verbose_name_plural': 'Organizaciones implementador',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'País meta',
                'verbose_name_plural': 'Países metas',
            },
        ),
        migrations.CreateModel(
            name='OrgSocias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('logo', sorl.thumbnail.fields.ImageField(upload_to='org-socias')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listas.Pais')),
            ],
            options={
                'verbose_name': 'Oganización socia',
                'verbose_name_plural': 'Organizaciones socias',
            },
        ),
    ]
