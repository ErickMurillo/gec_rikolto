# Generated by Django 2.2 on 2020-11-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poa', '0012_auto_20201029_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='subactividadespoa',
            name='ajuste',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='subactividadespoa',
            name='total',
            field=models.FloatField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
