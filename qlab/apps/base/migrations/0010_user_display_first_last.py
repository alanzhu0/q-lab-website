# Generated by Django 4.2.2 on 2023-11-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0009_alter_resource_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="display_first_last",
            field=models.BooleanField(
                default=False, verbose_name="Display first/last name"
            ),
        ),
    ]
