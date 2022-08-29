# Generated by Django 4.1 on 2022-08-28 12:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensor",
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
                (
                    "sensor_id",
                    models.CharField(
                        blank=True,
                        default=uuid.UUID("b1cf7bf7-71cd-46b8-8893-12f70188b0f4"),
                        max_length=100,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("unit", models.CharField(max_length=500)),
            ],
        ),
    ]
