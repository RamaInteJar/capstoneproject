# Generated by Django 4.1 on 2023-11-16 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commublog', '0002_remove_comment_create_date_comment_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 16, 19, 43, 12, 719393, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 16, 19, 43, 12, 719001, tzinfo=datetime.timezone.utc)),
        ),
    ]