# Generated by Django 4.1 on 2023-11-18 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commublog', '0017_alter_comment_created_date_alter_post_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 13, 20, 2, 574783, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 13, 20, 2, 575130, tzinfo=datetime.timezone.utc)),
        ),
    ]
