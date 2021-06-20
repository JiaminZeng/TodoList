"""TodoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Planer.views import user
from Planer.views import plan
from Planer.views import daily
from Planer.views import thing

urlpatterns = [

    url(r'^/', user.LoginView.as_view()),

    url(r'^admin/', admin.site.urls),

    url(r'^login/', user.LoginView.as_view()),
    url(r'^register/', user.RegisterView.as_view()),
    url(r'^refresh/', user.Refresh.as_view()),

    url(r'^buildPlan/', plan.BuildPlan.as_view()),
    url(r'^getPlan/', plan.GetPlan.as_view()),
    url(r'^changePlan/', plan.ChangePlan.as_view()),
    url(r'^finishPlan/', plan.FinishPlan.as_view()),

    url(r'^buildDaily/', daily.BuildDaily.as_view()),
    url(r'^getDaily/', daily.GetDaily.as_view()),
    url(r'^changDaily/', daily.ChangDaily.as_view()),
    url(r'^finishDaily/', daily.FinishDaily.as_view()),

    url(r'^getThing/', thing.GetThing.as_view()),
    url(r'^createThing/', thing.CreateThing.as_view()),
    url(r'^changeThing/', thing.ChangeThing.as_view()),
    url(r'^exchangeAction/', thing.ExchangeAction.as_view()),
    url(r'^getChangeHistory/', thing.GetChangeHistory.as_view()),

]
