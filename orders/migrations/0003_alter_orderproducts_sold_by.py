# Generated by Django 4.0.4 on 2022-05-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderproducts_sold_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='sold_by',
            field=models.CharField(max_length=100),
        ),
    ]