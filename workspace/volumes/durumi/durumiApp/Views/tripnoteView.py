from ..Models import MapModel
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..Models.UserModel import Tripnote
from ..apicodes import keyword
import simplejson as json
import os
import sys

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def InsertTripnote(name, dest, cat, userId):
    # Tripnote 생성시에는 장소와 카테고리가 비어있으므로 name 과 userId만 저장
    Tripnote(name=name, userId=userId).save()


def ReadTripnoteListFromDB(userId):
    TripnoteList = Tripnote.object.filter(userId=userId)

    return TripnoteList


def ReadTripnoteFromDB(userId, name):
    TripnoteList = Tripnote.object.filter(userId=userId, name=name)

    return TripnoteList


def tripnoteView(request):
    template_name = 'durumiApp/Tripnote.html'
    # ID = request.session("ID") 이런식으로 ID 받아오자
    # tripnoteList = ReadTripnoteFromDB(ID = ID) 이런식으로 DB에서 해당 ID의 트립노트 받아오기
    Test = ["test1", "test2", "test3"]
    userId = request.session["userId"]
    result = ReadTripnoteListFromDB(userId)
    #tripnote = MapModel.Tripnote.objects.all()
    context = {

        "Test": Test,
        "result": result
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


def selectTripnote(request):
    template_name = 'durumiApp/Tripnote.html'
    try:
        name = request.POST.get("name", "")
        userId = request.session["userId"]

    except (KeyError, name == "", userId == ""):
        result = '실패'
        context = {
            "result": result
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        result = ReadTripnoteFromDB(userId, name)
        context = {
            "result": result
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
