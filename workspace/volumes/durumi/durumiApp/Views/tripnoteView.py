# -*- coding:utf-8 -*-

from ..Models import MapModel
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..Models.UserModel import Tripnote
from ..Models.UserModel import User
from ..Models.UserModel import DurumiCat,AchieveClear, AchieveInfo
from ..apicodes import searchAPI as sa
from ..apicodes import keyword
import simplejson as json
import os
import sys

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

@csrf_exempt
def select(request,pageName):
    return globals()[pageName](request)


@csrf_exempt  # 보안문제로 적어줌
def selectTripnoteForaddTripnote(request):
    result = []
    userId = request.session['userId']
    user = User.objects.filter(userId=userId)[0]
    result = Tripnote.objects.filter(userId=user)
    retItems = {}
    i = 0
    for item in result:
        items = item.name
        retItems['TripnoteForadd'+str(i)] = items
        i += 1

    # tripnote = MapModel.Tripnote.objects.all()
    context = {

        "result": retItems,
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt  # 보안문제로 적어줌
def addTripnote(request):
    loginId = request.session['userId']
    id = User.objects.filter(userId = loginId)[0].id
    userAch = AchieveClear.objects.filter(userId_id = id)[0]
    if userAch.Achieve1 == False:
        userAch.Achieve1 = True
        userAch.save()
    contentid = request.POST.get("contentid", "")
    tripnoteName = request.POST.get("tripnoteName", "")
    userId = request.session['userId']
    user = User.objects.filter(userId=userId)[0]
    place = json.loads(sa.codeFindAPI(contentid)['item0'])
    # 여기부터 해야함 , 어떤 Tripnote에 넣을지 선택하는 창 만들고 거기서 입력받은 Tripnote에
    # 해당 장소의 정보를 넣어주면 됨
    Tn = Tripnote.objects.filter(name=tripnoteName, userId=user)[0]
    if Tn.dest:
        Tn.dest += "~"+str(place['title'])+":"+str(place['contentid'])
        Tn.cat += "~"+str(place['cat3'])
    else:
        Tn.dest += str(place['title']) + ":" + str(place['contentid'])
        Tn.cat += str(place['cat3'])

    Tn.save()
    context = {

    }
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt  # 보안문제로 적어줌
def addTripnoteList(request):
    try:
        tripnoteName = request.POST.get("TripnoteListNameBox", "")
        userId = request.session['userId']
        user = User.objects.filter(userId=userId)[0]
    except (KeyError, tripnoteName == ""):
        result = '실패'
        context = {
            "result": result
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        #size = len(Tripnote.objects.filter()) + 1
        Tripnote(dest="", cat="",
                 name=tripnoteName, userId=user).save()
        # Tripnote 생성시에는 장소와 카테고리가 비어있으므로 name 과 userId만 저장
        # userId 넣는 코드 만들어야함 현재는 유저정보가 없어서 외래키를 지정할 수 없음
        result = '성공'
        context = {
            "result": result
        }
        return HttpResponse(json.dumps(context), content_type="application/json")


def InsertPlace(name, dest, cat, userId):
    tripnote = Tripnote.object.filter(userId=userId, name=name)[0]
    tripnote.dest += dest + "~"
    tripnote.cat += cat + "~"
    tripnote.save()


def ReadTripnoteListFromDB(userId):
    TripnoteList = Tripnote.objects.filter(userId=userId)

    return TripnoteList


def ReadTripnoteFromDB(name):
    # PlaceList = Tripnote.objects.filter(userId=userId, name=name)
    PlaceList = Tripnote.objects.filter(name=name)
    return PlaceList


@csrf_exempt  # 보안문제로 적어줌
def tripnoteView(request):
    template_name = 'durumiApp/tripnote.html'
    # userId = request.session["userId"]

    userId = request.session['userId']

    result = []
    user = User.objects.filter(userId=userId)[0]

    result = Tripnote.objects.filter(userId=user)
    retItems = {}
    i = 0
    for item in result:
        items = item.name
        retItems['Tripnote'+str(i)] = items
        i += 1

    # tripnote = MapModel.Tripnote.objects.all()
    context = {

        "result": retItems,
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt  # 보안문제로 적어줌
def selectTripnote(request):
    template_name = 'durumiApp/tripnote.html'
    try:
        # req = json.loads(request.body)
        # name = req['name']
        tripnoteName = request.POST.get("name", "")
        userId = request.session['userId']
        user = User.objects.filter(userId=userId)[0]
        # name = request.POST["name"]
        # userId = request.session["userId"]
        # return render(request, 'durumiApp/test.html', {"name": "mmmmmmmmmm"})
    except (KeyError):
        result = '실패'
        context = {
            "result": result
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        DurumiCat(durumiDesc="관광지", iconAddr="/static/image/icons/13.png").save()
        # tripNote = ReadTripnoteFromDB(userId=userId, name=name)

        tripNote = Tripnote.objects.filter(name=tripnoteName, userId=user)[0]

        retItems = {}

        i = 0
        dests = []
        cats = []
        codes = []
        # dests_codes = tripNote.dest.split('~')
        dests = tripNote.dest.split('~')
        cats = tripNote.cat.split('~')

        for dest,   cat in zip(dests,   cats):
            DurumiCat(durumiDesc=cat).save()
            category = []

            category = DurumiCat.objects.filter(durumiDesc=cat)

            for c in category:
                cat_ = c.iconAddr

                d = dest.split(':')
                dest_ = d[0]
                code_ = d[1]
            # cat = "/static/image/icons/13.png"
            # 여기 윗부분 카테고리 아이콘 하는 방식에 따라 수정해야함
            place = json.loads(sa.codeFindAPI(code_)['item0'])

            item = {}

            item['cat'] = cat_
            item['dest'] = dest_
            item['code'] = code_
            item['mapx'] = str(place['mapx'])
            item['mapy'] = str(place['mapy'])
            item['place'] = place
            retItems['TripnotePlace'+str(i)] = item
            i += 1

        context = {
            "Test": request.POST.get("name", ""),
            "result": retItems,
            "items": item
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
