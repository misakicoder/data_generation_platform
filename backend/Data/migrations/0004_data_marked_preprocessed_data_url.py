# Generated by Django 4.1 on 2024-04-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Data", "0003_remove_data_data_url_data_cleaned_data_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="marked_preprocessed_data_url",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
