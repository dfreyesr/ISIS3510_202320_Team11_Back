# Generated by Django 4.2.5 on 2023-09-27 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_alter_accesspoint_dateafter_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="trailer", name="volume", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="accesspoint",
            name="dateAfter",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 26, 19, 34, 40, 592249)
            ),
        ),
        migrations.AlterField(
            model_name="accesspoint",
            name="dateBefore",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 26, 19, 34, 40, 592249)
            ),
        ),
        migrations.AlterField(
            model_name="load", name="volume", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="trailer", name="dropoff", field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="trailer", name="pickup", field=models.CharField(max_length=30),
        ),
    ]
