# Generated by Django 2.1 on 2018-10-15 08:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('daigo', '0002_auto_20181015_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 15, 8, 25, 22, 692074, tzinfo=utc)),
        ),
    ]
