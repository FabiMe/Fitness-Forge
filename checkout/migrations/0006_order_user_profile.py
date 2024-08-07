# Generated by Django 3.2.25 on 2024-04-28 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("checkout", "0005_auto_20240428_1659"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="user_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="profiles.userprofile",
            ),
        ),
    ]
