# Generated by Django 4.1 on 2022-08-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sensor", "0005_data_sensor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="value",
            field=models.FloatField(),
        ),
    ]