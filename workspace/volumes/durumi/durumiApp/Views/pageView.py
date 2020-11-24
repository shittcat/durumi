from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..apicodes import keyword
from ..Models.UserModel import User, Notice, AchieveClear, AchieveInfo
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

@csrf_exempt  # 보안문제로 적어줌
def viewPage(request, pageName):  # 맵 템플릿 연결
    template_name = 'durumiApp/viewPage/'+pageName+'.html'
    if pageName == "viewNotice":
        context = loadNotice()
    elif pageName == "viewQuestion":
        try : 
            if request.session['loginOk'] == False:
                pass
        except : 
            request.session['loginOk'] = False
        if request.session['loginOk'] == False:
            context = {
                "userMail": "404"
            }
        else:
            context = loadEmail(request.session['userId'])
    elif pageName == "viewAcv":
        loginId = request.session['userId']
        context = AcvPack(loginId)
    else:
        context = {
            "test": "viewInfo test",
        }

    return render(request, template_name, context)

@csrf_exempt  # 보안문제로 적어줌
def loadNotice():
    timeNow = datetime.now()
    timeYearAgo = timeNow + timedelta(days=-365)
    noticeList = Notice.objects.filter(pubDate__range=(timeYearAgo, timeNow)).order_by('-id')
    context = {
        "noticeList": noticeList
    }
    return context

@csrf_exempt  # 보안문제로 적어줌
def loadEmail(sessionId):
    context = {
        "userMail": User.objects.filter(userId=sessionId)[0].userMail
        }
    return context

@csrf_exempt  # 보안문제로 적어줌
def AcvPack(loginId):
    acvInfo = AchieveInfo.objects.values()
    numofAcv = acvInfo.count()
    
    id = User.objects.filter(userId = loginId)[0].id
    clear = AchieveClear.objects.filter(userId_id = id).values()
    clearlst = list(clear[0].values())
    clearlst.pop(0)
    clearlst.pop(0)
    
    acvLst=[]

    for i in range(numofAcv):
        acv = acvInfo[i]
        acv.update(clear = clearlst[i])
        addr = 'image/Achv/' + acv.get('imgAddr') + '.png'
        acv.update(imgAddr = addr)
        acvLst.append(acv)
    
    context = {
        "Acv": acvLst,
        "numofAcv": numofAcv,
    }
    return context