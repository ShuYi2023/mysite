# Generated by Django 4.1.10 on 2023-10-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0004_articlepost_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="articlepost",
            name="for_vip",
            field=models.BooleanField(default=False),
        ),
    ]
