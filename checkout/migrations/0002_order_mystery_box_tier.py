# Generated by Django 3.2.25 on 2024-04-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mystery_box_tier',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]