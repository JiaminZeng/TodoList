# Generated by Django 3.1.7 on 2021-05-31 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DateApp', '0004_auto_20210531_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='changehistory',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]