# Generated by Django 4.1 on 2024-04-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Data", "0002_data_data_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="data",
            name="data_url",
        ),
        migrations.AddField(
            model_name="data",
            name="cleaned_data_url",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="data",
            name="marked_data_url",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="data",
            name="ori_data_url",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="data",
            name="preprocessed_data_url",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
