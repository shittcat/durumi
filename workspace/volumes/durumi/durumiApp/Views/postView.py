from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..Models.UserModel import Question
import simplejson as json
import os
import sys

@csrf_exempt
def select(request,pageName):
    return globals()[pageName](request)

@csrf_exempt  # 보안문제로 적어줌
def sendQuestion(request):
    template_name = 'durumiApp/viewpage/viewQuestion.html'
    data = request.POST
    if data['title'] == "" or data ['email'] == "" or data['content'] == "":
        context = {
            "result" : "누락된 내용이 있습니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif (data['email'] != "") and ('@' not in data['email']):
        context = {
            "result" : "올바른 이메일 형식이 아닙니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    
    timeNow = datetime.now()

    question = Question(title = data['title'], email = data['email'], content = ['content'], pubDate = timeNow)
    question.save()
    
    context = {
        "result": "ok"
    }
    return HttpResponse(json.dumps(context), content_type="application/json")