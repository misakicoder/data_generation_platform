# Generated by Django 4.1 on 2024-04-13 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Data", "0007_data_task_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="ori_data_cols",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cols", models.CharField(max_length=10000)),
                (
                    "data_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Data.data"
                    ),
                ),
            ],
        ),
    ]
