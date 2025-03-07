# Generated by Django 4.1.10 on 2023-10-05 13:07

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("article", "0003_articlecolumn_articlepost_column"),
    ]

    operations = [
        migrations.AddField(
            model_name="articlepost",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
