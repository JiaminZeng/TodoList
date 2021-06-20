import datetime
import time
from .tokens import create_token, get_username
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from DateApp import models


class BuildDaily(APIView):

    def post(self, request, *args, **kwargs):
        _content = request.data["content"]
        _reward = request.data["reward"]
        _token = request.data["token"]
        _user = get_username(_token)
        ret = {
            'code': 1,
        }
        try:
            id = models.User.objects.filter(username=_user)[0].pk
            models.Daily.objects.create(attribution=id, content=_content,
                                       reward=_reward, state=0)
        except:
            ret['code'] = -1

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class ChangDaily(APIView):

    def post(self, request, *args, **kwargs):
        _id = request.data["id"]
        _content = request.data["content"]
        _reward = request.data["reward"]
        _token = request.data["token"]
        _user=get_username(_token)
        id = models.User.objects.filter(username=_user)[0].pk
        ret = {'code': 1}
        try:
            if _content==-1:
                models.Daily.objects.filter(pk=_id, attribution=id).delete()
            else:
                models.Daily.objects.filter(pk=_id, attribution=id).update(reward=_reward, content=_content)
        except:
            ret['code'] = -1
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class GetDaily(APIView):

    def post(self, request, *args, **kwargs):
        _state = request.data["state"]
        _token = request.data["token"]
        _user = get_username(_token)
        id = models.User.objects.filter(username=_user)[0].pk
        planList = models.Daily.objects.filter(attribution=id, state=_state)
        ret = []
        for plan in planList:
            tp = model_to_dict(plan)
            ret.append(tp)
        response = JsonResponse(ret ,safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class FinishDaily(APIView):

    def post(self, request, *args, **kwargs):
        _planId = request.data["planId"]
        _token = request.data["token"]
        _user = get_username(_token)
        id = models.User.objects.filter(username=_user)[0].pk

        _curTime = datetime.datetime.now()
        _daily = models.User.objects.filter(username=_user)[0].totalDailyTasks
        _reward = models.User.objects.filter(username=_user)[0].remainingRewards
        _add = models.Daily.objects.filter(pk=_planId, attribution=id)[0].reward
        models.Daily.objects.filter(state=0, pk=_planId, attribution=id).update(state=1, endTime=_curTime)
        models.User.objects.filter(username=_user).update(remainingRewards=_reward+_add,totalDailyTasks=_daily+1)

        ret = {'code': 1}
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response