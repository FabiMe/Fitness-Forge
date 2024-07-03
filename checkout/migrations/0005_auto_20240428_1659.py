# Generated by Django 3.2.25 on 2024-04-28 16:59

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0004_alter_order_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="billing_country",
            field=django_countries.fields.CountryField(
                blank=True, max_length=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="billing_county",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="billing_postcode",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="billing_street_address1",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="billing_street_address2",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="billing_town_or_city",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
