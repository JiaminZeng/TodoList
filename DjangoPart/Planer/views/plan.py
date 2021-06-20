import datetime
import time
from .tokens import create_token, get_username
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from DateApp import models


class BuildPlan(APIView):

    def post(self, request, *args, **kwargs):

        _content = request.data["content"]
        _endTime = request.data["endTime"]
        _reward = request.data["reward"]
        _token = request.data["token"]
        _user = get_username(_token)

        _curTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        ret = {
            'code': '1',
        }

        try:
            id = models.User.objects.filter(username=_user)[0].pk
            models.Plan.objects.create(attribution=id, content=_content, buildTime=_curTime, endTime=_endTime,
                                       reward=_reward, state=0)
        except:
            ret['code'] = '-1'

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class GetPlan(APIView):

    def post(self, request, *args, **kwargs):
        _state = request.data["state"]
        _token = request.data["token"]
        _user = get_username(_token)
        id = models.User.objects.filter(username=_user)[0].pk
        _st = datetime.datetime(2000, 1, 1)
        _ed = datetime.datetime.now()
        if _state == 1:
            planList = models.Plan.objects.filter(attribution=id, state=1)
        elif _state == 2:
            planList = models.Plan.objects.filter(attribution=id, state=0, endTime__range=(_st, _ed))
        else:
            _st = datetime.datetime.now()
            _ed = datetime.datetime(2099, 1, 1)
            planList = models.Plan.objects.filter(attribution=id, state=0, endTime__range=(_st, _ed))

        ret = []
        for plan in planList:
            tp = model_to_dict(plan)
            ret.append(tp)
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class ChangePlan(APIView):

    def post(self, request, *args, **kwargs):
        _id = request.data["id"]
        _content = request.data["content"]
        _endTime = request.data["endTime"]
        _reward = request.data["reward"]
        _token = request.data["token"]
        _user = get_username(_token)
        id = models.User.objects.filter(username=_user)[0].pk
        ret = {'code': 1}
        try:
            if _content == -1:
                models.Plan.objects.filter(pk=_id, attribution=id).delete()
            else:
                models.Plan.objects.filter(pk=_id, attribution=id).update(content=_content, endTime=_endTime,
                                                                          reward=_reward)
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


class FinishPlan(APIView):

    def post(self, request, *args, **kwargs):
        _planId = request.data["planId"]
        _token = request.data["token"]
        _user = get_username(_token)
        _curTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        id = models.User.objects.filter(username=_user)[0].pk

        _plan = models.User.objects.filter(username=_user)[0].totalPlanTasks
        _reward = models.User.objects.filter(username=_user)[0].remainingRewards
        _add = models.Plan.objects.filter(pk=_planId, attribution=id)[0].reward
        models.Plan.objects.filter(state=0, pk=_planId, attribution=id).update(state=1, endTime=_curTime)
        models.User.objects.filter(username=_user).update(remainingRewards=_reward + _add, totalPlanTasks=_plan + 1)

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
