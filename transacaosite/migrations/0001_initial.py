# Generated by Django 2.1 on 2019-01-02 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apisite', '0002_auto_20190102_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_item', models.CharField(max_length=35)),
                ('valor_item', models.IntegerField()),
            ],
            options={
                'verbose_name': 'item do jogo',
                'verbose_name_plural': 'itens',
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_pagseguro', models.CharField(blank=True, max_length=60, unique=True)),
                ('item_pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item_pedido', to='transacaosite.Item')),
                ('usuario_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_pedido', to='apisite.Inventario')),
            ],
        ),
    ]
