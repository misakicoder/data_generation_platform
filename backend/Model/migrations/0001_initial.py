# Generated by Django 4.1 on 2024-04-04 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Model",
            fields=[
                ("model_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("model_name", models.CharField(max_length=100)),
                ("model_description", models.CharField(max_length=10000)),
                ("model_url", models.CharField(max_length=1000)),
                ("task_type", models.CharField(max_length=100)),
            ],
        ),
    ]
