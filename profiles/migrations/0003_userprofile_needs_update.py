# Generated by Django 3.2.25 on 2024-05-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0002_alter_userprofile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="needs_update",
            field=models.BooleanField(default=False),
        ),
    ]
