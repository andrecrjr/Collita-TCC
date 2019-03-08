# Generated by Django 2.1 on 2019-03-08 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transacaosite', '0002_item_utilizavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_in_inventario', to='transacaosite.Item'),
        ),
        migrations.AlterField(
            model_name='carrinho',
            name='transacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_to_transacao', to='transacaosite.Transacao'),
        ),
    ]
