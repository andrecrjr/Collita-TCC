# Generated by Django 2.1 on 2019-02-23 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apisite', '0003_auto_20190107_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_boleto', models.BooleanField(default=False, verbose_name='Status do boleto')),
                ('item_comprado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_usuario', to='transacaosite.Item')),
                ('usuario_transacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacao_inventario', to='apisite.Inventario')),
            ],
            options={
                'verbose_name': 'transação do site',
                'verbose_name_plural': 'transações do site',
                'db_table': 'transacao',
            },
        ),
    ]
