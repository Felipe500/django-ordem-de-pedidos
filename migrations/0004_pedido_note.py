# Generated by Django 3.2.6 on 2021-09-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210820_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
