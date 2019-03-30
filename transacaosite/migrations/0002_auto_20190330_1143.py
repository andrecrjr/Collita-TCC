# Generated by Django 2.1 on 2019-03-30 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transacaosite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='utilizavel',
        ),
        migrations.AlterField(
            model_name='transacao',
            name='item_comprado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_usuario', to='transacaosite.ItemCompra'),
        ),
    ]