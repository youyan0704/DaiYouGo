# Generated by Django 2.1 on 2018-10-18 07:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('xauth', '0002_auto_20181018_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSystemMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activate', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xauth.SystemMenu')),
            ],
            options={
                'db_table': 'xauth_group_system_menu',
            },
        ),
        migrations.AlterField(
            model_name='systemhistory',
            name='operator_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 7, 8, 35, 276225, tzinfo=utc)),
        ),
    ]
