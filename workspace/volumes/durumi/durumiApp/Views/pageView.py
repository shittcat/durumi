from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..apicodes import keyword
from ..Models.UserModel import Notice

import simplejson as json
import os
import sys

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))



def viewBase(request):  # 맵 템플릿 연결
    template_name = 'durumiApp/viewPage/viewBase.html'
    context = {
        "test": "viewBase test",
    }
    return render(request, template_name, context)


def viewPage(request, pageName):  # 맵 템플릿 연결
    template_name = 'durumiApp/viewPage/'+pageName+'.html'
    if pageName == "viewNotice":
        context = loadNotice()
    else:
        context = {
            "test": "viewInfo test",
        }
    return render(request, template_name, context)

@csrf_exempt  # 보안문제로 적어줌
def loadNotice():
    timeNow = datetime.now()
    timeYearAgo = timeNow + timedelta(hours=-365)
    noticeList = Notice.objects.filter(pubDate__range=(timeYearAgo, timeNow)).order_by('-id')
    context = {
        "noticeList": noticeList
    }
    return context