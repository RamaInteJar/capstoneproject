# Generated by Django 4.1 on 2023-11-16 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commublog', '0004_alter_comment_created_date_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 16, 23, 59, 52, 166938, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 16, 23, 59, 52, 166534, tzinfo=datetime.timezone.utc)),
        ),
    ]
