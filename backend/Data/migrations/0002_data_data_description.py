# Generated by Django 4.1 on 2024-04-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Data", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="data_description",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
