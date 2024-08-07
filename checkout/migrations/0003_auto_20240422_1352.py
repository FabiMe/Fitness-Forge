# Generated by Django 3.2.25 on 2024-04-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0002_order_mystery_box_tier"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderlineitem",
            name="first_name",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="orderlineitem",
            name="last_name",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="orderlineitem",
            name="voucher_type",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
