# Generated by Django 2.1 on 2018-10-19 02:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('xauth', '0003_auto_20181018_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemhistory',
            name='operator_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 19, 2, 7, 52, 272954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='systemmenu',
            name='action',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
