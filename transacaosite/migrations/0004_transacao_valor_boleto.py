# Generated by Django 2.1 on 2019-05-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacaosite', '0003_auto_20190509_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='valor_boleto',
            field=models.CharField(default=0, max_length=25),
        ),
    ]