# Generated by Django 3.0.9 on 2020-10-07 19:18

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo_gerencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndObjetivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicador', smart_selects.db_fields.ChainedForeignKey(chained_field='objetivo', chained_model_field='objetivo', on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.IndicadoresObjetivos')),
                ('objetivo', smart_selects.db_fields.ChainedForeignKey(chained_field='proyecto', chained_model_field='proyecto', on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.Objetivo')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.Proyecto')),
            ],
            options={
                'verbose_name': 'Indicadores de Objetivo',
                'verbose_name_plural': 'Indicadores de Objetivos',
            },
        ),
        migrations.CreateModel(
            name='ObjInd4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('nombre_plataforma', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre de Plataforma')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado_plataforma', models.CharField(blank=True, choices=[('No iniciado', 'No iniciado'), ('Iniciado', 'Iniciado'), ('Avanzado', 'Avanzado'), ('Cumplido', 'Cumplido')], max_length=100, null=True, verbose_name='Estado de Plataforma')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='obj-indicador-4/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndObjetivos')),
            ],
            options={
                'verbose_name': 'Indicador 4',
                'verbose_name_plural': 'Indicador 4',
            },
        ),
        migrations.CreateModel(
            name='ObjInd3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('nombre_politica_regional', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre de Pólitica Regional')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado_esfuerzo', models.CharField(blank=True, choices=[('No iniciado', 'No iniciado'), ('Iniciado', 'Iniciado'), ('Avanzado', 'Avanzado'), ('Cumplido', 'Cumplido')], max_length=100, null=True, verbose_name='Estado de esfuerzo')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='obj-indicador-3/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndObjetivos')),
            ],
            options={
                'verbose_name': 'Indicador 3',
                'verbose_name_plural': 'Indicador 3',
            },
        ),
        migrations.CreateModel(
            name='ObjInd2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_productores', models.IntegerField(blank=True, null=True, verbose_name='Número de productores')),
                ('productividad_cacao', models.FloatField(blank=True, null=True, verbose_name='Productividad cacao kg/ha')),
                ('aumento_productividad_cacao', models.FloatField(blank=True, null=True, verbose_name='Aumento de productividad (%)')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='obj-indicador-2/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndObjetivos')),
            ],
            options={
                'verbose_name': 'Indicador 2',
                'verbose_name_plural': 'Indicador 2',
            },
        ),
        migrations.CreateModel(
            name='ObjInd1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_productores', models.IntegerField(blank=True, null=True, verbose_name='Número de productores')),
                ('ingreso_saf', models.FloatField(blank=True, null=True, verbose_name='Ingreso de SAF USD/ha')),
                ('aumento_ingreso_saf', models.FloatField(blank=True, null=True, verbose_name='Aumento de Ingreso SAF (%)')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='obj-indicador-1/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndObjetivos')),
            ],
            options={
                'verbose_name': 'Indicador 1',
                'verbose_name_plural': 'Indicador 1',
            },
        ),
        migrations.CreateModel(
            name='IndProductos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicador', smart_selects.db_fields.ChainedForeignKey(chained_field='producto', chained_model_field='producto', on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.IndicadoresProductos')),
                ('producto', smart_selects.db_fields.ChainedForeignKey(chained_field='proyecto', chained_model_field='proyecto', on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.Producto')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.Proyecto')),
            ],
            options={
                'verbose_name': 'Indicadores de Productos',
                'verbose_name_plural': 'Indicadores de Productos',
            },
        ),
        migrations.CreateModel(
            name='IndProducto2_6_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_politica', models.IntegerField(blank=True, null=True, verbose_name='Número de Instrumentos y mecanismos para implementación y seguimiento de estrategia regional')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-2-6-2/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 2.6.2',
                'verbose_name_plural': 'Indicador 2.6.2',
            },
        ),
        migrations.CreateModel(
            name='IndProducto2_6_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_politica', models.IntegerField(blank=True, null=True, verbose_name='Número de pólitica en implementación en marco de CAC')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-2-6-1/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 2.6.1',
                'verbose_name_plural': 'Indicador 2.6.1',
            },
        ),
        migrations.CreateModel(
            name='IndProducto2_5_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_plataformas', models.IntegerField(blank=True, null=True, verbose_name='Número de plataformas nacionales funcionando')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-2-5-2/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 2.5.2',
                'verbose_name_plural': 'Indicador 2.5.2',
            },
        ),
        migrations.CreateModel(
            name='IndProducto2_5_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_comite', models.IntegerField(blank=True, null=True, verbose_name='Número de Comité de Integración del Cacao de Centroamérica y Caribe  establecida y funcionando')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-2-5-1/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 2.5.1',
                'verbose_name_plural': 'Indicador 2.5.1',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_4_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_estudio', models.IntegerField(blank=True, null=True, verbose_name='Número de estudio sobre el nivel de conocimiento y uso de directrices para fomento de cacao resiliente')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-4-4/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.4.4',
                'verbose_name_plural': 'Indicador 1.4.4',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_4_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_documentos', models.IntegerField(blank=True, null=True, verbose_name='Número de documento con directrices regionales para modelo de negocios inclusivos')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-4-3/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.4.3',
                'verbose_name_plural': 'Indicador 1.4.3',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_4_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_documentos', models.IntegerField(blank=True, null=True, verbose_name='Número de documento con directrices regionales para fomento de Cacao resiliente')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-4-2/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.4.2',
                'verbose_name_plural': 'Indicador 1.4.2',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_4_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_documentos', models.IntegerField(blank=True, null=True, verbose_name='Número de documento sobre el impacto de Cambio Climático en zonas cacaoteras')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-4-1/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.4.1',
                'verbose_name_plural': 'Indicador 1.4.1',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_3_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_actores', models.IntegerField(blank=True, null=True, verbose_name='Número de actores claves de la cadena que usan TICS y plataformas digitales')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-3-3/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.3.3',
                'verbose_name_plural': 'Indicador 1.3.3',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_3_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_experiencias', models.IntegerField(blank=True, null=True, verbose_name='Número de experiencias y casos de éxito sistematizado')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-3-2/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.3.2',
                'verbose_name_plural': 'Indicador 1.3.2',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_3_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_participantes', models.IntegerField(blank=True, null=True, verbose_name='Número de participantes quienes hace uso de los materiales generados pro el proyecto')),
                ('numero_eventos', models.IntegerField(blank=True, null=True, verbose_name='Numero de eventos o iniciativas para difundir el uso de materiales generados por el proyecto')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-3-1/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.3.1',
                'verbose_name_plural': 'Indicador 1.3.1',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_2_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_estudio', models.IntegerField(blank=True, null=True, verbose_name='Número de estudio sobre el efecto de modelos de inversión NI y SAF')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-2-5/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.2.5',
                'verbose_name_plural': 'Indicador 1.2.5',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_2_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_ofertas', models.IntegerField(blank=True, null=True, verbose_name='Número de oferta de servicios técnicos identificada, homologada y difundida')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-2-4/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.2.4',
                'verbose_name_plural': 'Indicador 1.2.4',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_2_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_modelos', models.IntegerField(blank=True, null=True, verbose_name='Número de modelos de inversión para validación')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-2-3/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.2.3',
                'verbose_name_plural': 'Indicador 1.2.3',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_2_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_iniciativas', models.IntegerField(blank=True, null=True, verbose_name='Número de iniciativas MNI identificado para replicar')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-2-2/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.2.2',
                'verbose_name_plural': 'Indicador 1.2.2',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_2_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_iniciativas', models.IntegerField(blank=True, null=True, verbose_name='Número de iniciativas de inversión MNI en marcha')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-2-1/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.2.1',
                'verbose_name_plural': 'Indicador 1.2.1',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_1_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_comunidades', models.IntegerField(blank=True, null=True, verbose_name='Número de comunidades de práctica en marcha')),
                ('numero_fincas', models.IntegerField(blank=True, null=True, verbose_name='Número de fincas pilotos en marcha')),
                ('numero_negocios', models.IntegerField(blank=True, null=True, verbose_name='Número de negocios inclusivos en marcha')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-1-3/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.1.3',
                'verbose_name_plural': 'Indicador 1.1.3',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_1_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('nombre_plan', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre del Plan')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-1-2/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.1.2',
                'verbose_name_plural': 'Indicador 1.1.2',
            },
        ),
        migrations.CreateModel(
            name='IndProducto1_1_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('nombre_estudio', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre del estudio')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-prod-1-1-1/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndProductos')),
            ],
            options={
                'verbose_name': 'Indicador 1.1.1',
                'verbose_name_plural': 'Indicador 1.1.1',
            },
        ),
        migrations.CreateModel(
            name='IndEfectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efecto', smart_selects.db_fields.ChainedForeignKey(chained_field='proyecto', chained_model_field='proyecto', on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.Efecto')),
                ('indicador', smart_selects.db_fields.ChainedForeignKey(chained_field='efecto', chained_model_field='efecto', on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.IndicadoresEfectos')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gerencia.Proyecto')),
            ],
            options={
                'verbose_name': 'Indicadores de Efectos',
                'verbose_name_plural': 'Indicadores de Efectos',
            },
        ),
        migrations.CreateModel(
            name='IndEfecto2_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('nombre_politica', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre de Pólitica/Estrategia actualizada')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado_esfuerzo', models.CharField(blank=True, choices=[('No iniciado', 'No iniciado'), ('Iniciado', 'Iniciado'), ('Avanzado', 'Avanzado'), ('Cumplido', 'Cumplido')], max_length=100, null=True, verbose_name='Estado de esfuerzo')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-efecto-2-1/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndEfectos')),
            ],
            options={
                'verbose_name': 'Indicador 2.1',
                'verbose_name_plural': 'Indicador 2.1',
            },
        ),
        migrations.CreateModel(
            name='IndEfecto1_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_empresas', models.IntegerField(blank=True, null=True, verbose_name='Número de empresas implementando MNC')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-efecto-1-2/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndEfectos')),
            ],
            options={
                'verbose_name': 'Indicador 1.2',
                'verbose_name_plural': 'Indicador 1.2',
            },
        ),
        migrations.CreateModel(
            name='IndEfecto1_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('semestre', models.IntegerField(choices=[(1, 'I'), (2, 'II')])),
                ('numero_productores', models.IntegerField(blank=True, null=True, verbose_name='Número de productores adoptando BPA')),
                ('porcentaje_mujeres', models.IntegerField(blank=True, null=True, verbose_name='% de mujeres adoptando BPA')),
                ('porentaje_jovenes', models.IntegerField(blank=True, null=True, verbose_name='% de Jovenes adoptando BPA')),
                ('fuente', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='ind-efecto-1-1/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo_indicadores.IndEfectos')),
            ],
            options={
                'verbose_name': 'Indicador 1.1',
                'verbose_name_plural': 'Indicador 1.1',
            },
        ),
    ]
