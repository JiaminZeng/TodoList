# Generated by Django 3.1.7 on 2021-05-31 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DateApp', '0002_auto_20210531_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily',
            name='buildTime',
        ),
        migrations.RemoveField(
            model_name='daily',
            name='endTime',
        ),
    ]