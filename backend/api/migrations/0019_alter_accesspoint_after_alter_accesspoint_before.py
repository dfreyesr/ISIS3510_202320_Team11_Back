# Generated by Django 4.2.5 on 2023-09-27 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0018_alter_accesspoint_after_alter_accesspoint_before"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accesspoint",
            name="after",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 27, 18, 48, 41, 906186)
            ),
        ),
        migrations.AlterField(
            model_name="accesspoint",
            name="before",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 27, 18, 48, 41, 906186)
            ),
        ),
    ]
