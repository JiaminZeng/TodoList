# Generated by Django 3.1.7 on 2021-05-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribution', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('afterChangeRewards', models.IntegerField()),
                ('buildTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ChangeThings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribution', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('totalGet', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribution', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('buildTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('state', models.IntegerField()),
                ('reword', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribution', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('buildTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('state', models.IntegerField()),
                ('reword', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribution', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('buildTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('state', models.IntegerField()),
                ('reword', models.IntegerField()),
                ('afterChangeRewards', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('remainingRewards', models.IntegerField()),
                ('totalDailyTasks', models.IntegerField()),
                ('totalPlanTasks', models.IntegerField()),
            ],
        ),
    ]
