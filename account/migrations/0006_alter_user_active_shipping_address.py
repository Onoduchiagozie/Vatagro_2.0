# Generated by Django 4.0.4 on 2022-05-16 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_shippingaddress_created_by_storelocation_created_by'),
        ('account', '0005_alter_user_active_shipping_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Active_Shipping_Address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='goods.shippingaddress'),
        ),
    ]