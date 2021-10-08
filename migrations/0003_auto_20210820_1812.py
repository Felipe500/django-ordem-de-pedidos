# Generated by Django 3.2.6 on 2021-08-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210820_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Saiu para entrega', 'Saiu para entrega'), ('Entregue', 'Entregue')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='category',
            field=models.CharField(choices=[('Interior', 'Interior'), ('Exterior', 'Exterior')], max_length=200, null=True),
        ),
    ]