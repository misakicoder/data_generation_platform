# Generated by Django 4.1 on 2024-04-04 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Algorithm",
            fields=[
                (
                    "algorithm_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("algorithm_name", models.CharField(max_length=100)),
                ("algorithm_description", models.CharField(max_length=10000)),
                ("task_type", models.CharField(max_length=100)),
            ],
        ),
    ]
