# Generated by Django 4.0.5 on 2022-07-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
