# Generated by Django 2.1 on 2019-04-19 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apisite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('nome_item', models.CharField(max_length=35)),
                ('valor_item', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagem_item', models.FileField(default='', upload_to='item_folder/', verbose_name='Imagem do item')),
            ],
            options={
                'verbose_name': 'item do jogo',
                'verbose_name_plural': 'itens',
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('id_usuario', models.BigIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_itens', to='transacaosite.Item')),
            ],
            options={
                'verbose_name': 'item da compra',
                'verbose_name_plural': 'items da compra',
                'db_table': 'item_transacao',
            },
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_boleto', models.BooleanField(default=False, verbose_name='Status do boleto')),
                ('codigo_boleto', models.CharField(default=0, max_length=45)),
                ('usuario_transacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacao_inventario', to='apisite.Inventario')),
            ],
            options={
                'verbose_name': 'transação do site',
                'verbose_name_plural': 'transações do site',
                'db_table': 'transacao',
            },
        ),
        migrations.AddField(
            model_name='itemcompra',
            name='item_transacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_transacao', to='transacaosite.Transacao'),
        ),
    ]
