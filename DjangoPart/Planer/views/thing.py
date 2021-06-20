import datetime
import time
from .tokens import create_token, get_username
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from DateApp import models


class CreateThing(APIView):

    def post(self, request, *args, **kwargs):
        _content = request.data["content"]
        _cost = request.data["cost"]
        _token = request.data["token"]
        _user = get_username(_token)
        ret = {
            'code': 1,
        }
        try:
            id = models.User.objects.filter(username=_user)[0].pk
            models.ChangeThings.objects.create(attribution=id, content=_content,
                                               cost=_cost, totalGet=0)
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


class GetThing(APIView):

    def post(self, request, *args, **kwargs):
        _token = request.data["token"]
        _user = get_username(_token)
        id = models.User.objects.filter(username=_user)[0].pk
        planList = models.ChangeThings.objects.filter(attribution=id)
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


class ChangeThing(APIView):

    def post(self, request, *args, **kwargs):
        _id = request.data["id"]
        _content = request.data["content"]
        _cost = request.data["cost"]
        _token = request.data["token"]
        _user = get_username(_token)
        id = models.User.objects.filter(username=_user)[0].pk
        ret = {'code': 1}
        try:
            if _content == -1 :
                models.ChangeThings.objects.filter(pk=_id, attribution=id).delete()
            else:
                models.ChangeThings.objects.filter(pk=_id, attribution=id).update(cost=_cost, content=_content)
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


class ExchangeAction(APIView):

    def post(self, request, *args, **kwargs):
        _id = request.data["id"]
        _token = request.data["token"]
        _user = get_username(_token)
        user = models.User.objects.filter(username=_user)[0]
        _remainingRewards = user.remainingRewards
        _user = user.id
        thing = models.ChangeThings.objects.filter(pk=_id)[0]
        _content = thing.content
        _cost = thing.cost
        _old = thing.totalGet
        _curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        ret = {'code': 1}
        if _remainingRewards >= _cost:
            _remainingRewards = _remainingRewards-_cost
            print(_remainingRewards)
            models.User.objects.filter(pk=_user).update(remainingRewards=_remainingRewards)
            models.ChangeThings.objects.filter(pk=_id).update(totalGet=_old + 1)
            models.ChangeHistory.objects.create(attribution=_user, content=_content,cost=_cost, buildTime=_curTime)
        else:
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


class GetChangeHistory(APIView):

    def post(self, request, *args, **kwargs):

        _token = request.data["token"]
        _user = get_username(_token)
        id = models.User.objects.filter(username=_user)[0].pk
        planList = models.ChangeHistory.objects.filter(attribution=id)
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

