# Generated by Django 4.1 on 2024-04-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Data", "0011_data_data_algorithm"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="data_algorithm",
            field=models.CharField(default="", max_length=100),
        ),
    ]
