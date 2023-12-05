# Generated by Django 4.2.5 on 2023-11-30 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0029_executiontime_alter_accesspoint_after_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ErrorLogs",
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
                ("function", models.CharField(max_length=50)),
                ("error_message", models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name="trailer",
            name="isAvailable",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="accesspoint",
            name="after",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 30, 18, 37, 34, 436274)
            ),
        ),
        migrations.AlterField(
            model_name="accesspoint",
            name="before",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 30, 18, 37, 34, 436274)
            ),
        ),
        migrations.AlterField(
            model_name="trailer",
            name="dropoff",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="trailer", name="pickup", field=models.CharField(max_length=200),
        ),
    ]
