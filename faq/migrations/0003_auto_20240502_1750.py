# Generated by Django 3.2.25 on 2024-05-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0002_auto_20240502_1736"),
    ]

    operations = [
        migrations.AddField(
            model_name="faq",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="faq",
            name="answer",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="faq",
            name="question",
            field=models.TextField(),
        ),
    ]
