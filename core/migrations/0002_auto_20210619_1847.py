# Generated by Django 3.2.3 on 2021-06-19 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('marca', models.CharField(max_length=20, verbose_name='Nombre de el producto')),
                ('modelo', models.CharField(max_length=20, verbose_name='Modelo del producto')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nomrbe del producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='CoolerGpu',
        ),
        migrations.DeleteModel(
            name='FuentePoder',
        ),
        migrations.DeleteModel(
            name='Gabinete',
        ),
        migrations.DeleteModel(
            name='PlacaMadre',
        ),
        migrations.DeleteModel(
            name='Procesador',
        ),
        migrations.DeleteModel(
            name='Ram',
        ),
        migrations.DeleteModel(
            name='TarjetaGrafica',
        ),
        migrations.DeleteModel(
            name='UnidadAlmacenamiento',
        ),
    ]
