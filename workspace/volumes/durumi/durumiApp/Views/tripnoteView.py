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


def InsertPlace(name, dest, cat, userId):
    tripnote = Tripnote.object.filter(userId=userId, name=name)[0]
    tripnote.dest += dest + "~"
    tripnote.cat += cat + "~"
    tripnote.save()


def ReadTripnoteListFromDB(userId):
    TripnoteList = Tripnote.object.filter(userId=userId)

    return TripnoteList


def ReadTripnoteFromDB(userId, name):
    PlaceList = Tripnote.object.filter(userId=userId, name=name)

    return PlaceList


@csrf_exempt  # 보안문제로 적어줌
def tripnoteView(request):
    template_name = 'durumiApp/Tripnote.html'
    #userId = request.session["userId"]
    #result = ReadTripnoteListFromDB(userId=userId)
    Tripnote(name="Test1", dest="광화문~종각~인사동~",
                      cat="관광지~관광지~관광지~", userId="J")
    retItems = {}
    i = 0
    for item in result:
        retItems['item'+str(i)] = json.dumps(item.name, ensure_ascii=False)
        i += 1
    #tripnote = MapModel.Tripnote.objects.all()
    context = {

        "Test": Test,
        "result": retItems
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
