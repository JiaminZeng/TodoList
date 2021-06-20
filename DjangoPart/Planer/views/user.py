import datetime
import time
from .tokens import create_token, get_username
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from DateApp import models


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.data["username"]
        pd = request.data["password"]
        result = models.User.objects.filter(username=user)
        ret = {
            'code': 1,
            'username': user,
        }

        if not result.exists() or result[0].password != pd:
            ret['code'] = -1
        else:
            _id=result[0].id
            _st = datetime.datetime(2000, 1, 1)
            _ed = datetime.datetime.today().date()
            _curTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
            models.Daily.objects.filter(state=1, attribution=_id, endTime__range=(_st, _ed)).update(state=0, endTime=_curTime )
            ret['token'] = create_token(user)
            ret['username'] = user
            ret['remainingRewards'] = result[0].remainingRewards
            ret['totalDailyTasks'] = result[0].totalDailyTasks
            ret['totalPlanTasks'] = result[0].totalPlanTasks


        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.data["username"]
        pd = request.data["password"]
        result = models.User.objects.filter(username=user)

        ret = {
            'code': 1,
            'username': user,
        }
        if result.exists():
            ret['code'] = -1
        else:
            ret['username'] = user
            ret['token'] = create_token(user)
            models.User.objects.create(username=user, password=pd, remainingRewards=0, totalDailyTasks=0,
                                       totalPlanTasks=0)

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response



class Refresh(APIView):

    def post(self, request, *args, **kwargs):
        _token = request.data["token"]
        _user = get_username(_token)
        ret={}
        result = models.User.objects.filter(username=_user)
        ret['remainingRewards'] = result[0].remainingRewards
        ret['totalDailyTasks'] = result[0].totalDailyTasks
        ret['totalPlanTasks'] = result[0].totalPlanTasks

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response