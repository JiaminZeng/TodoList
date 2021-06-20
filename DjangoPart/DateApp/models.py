from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    remainingRewards = models.IntegerField()
    totalDailyTasks = models.IntegerField()
    totalPlanTasks = models.IntegerField()


class Plan(models.Model):
    attribution = models.IntegerField()
    content = models.CharField(max_length=100)
    buildTime = models.DateTimeField()
    endTime = models.DateTimeField()
    state = models.IntegerField()
    reward = models.IntegerField()


class Daily(models.Model):
    attribution = models.IntegerField()
    content = models.CharField(max_length=100)
    endTime = models.DateTimeField(null=True, blank=True)
    state = models.IntegerField()
    reward = models.IntegerField()


class ChangeThings(models.Model):
    attribution = models.IntegerField()
    content = models.CharField(max_length=100)
    cost = models.IntegerField()
    totalGet = models.IntegerField()


class ChangeHistory(models.Model):
    attribution = models.IntegerField()
    content = models.CharField(max_length=100)
    cost=models.IntegerField(default=0)
    buildTime = models.DateTimeField()
