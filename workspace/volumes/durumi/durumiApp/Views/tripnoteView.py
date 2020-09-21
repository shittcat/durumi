# -*- coding:utf-8 -*-

from ..Models import MapModel
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..Models.UserModel import Tripnote
from ..Models.UserModel import User
from ..Models.UserModel import DurumiCat
from ..apicodes import searchAPI as sa
from ..apicodes import keyword
import simplejson as json
import os
import sys

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def addTripnote(name, dest, cat, userId):
    # Tripnote 생성시에는 장소와 카테고리가 비어있으므로 name 과 userId만 저장
    
    Tripnote(name=name, userId=userId).save()


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
    # result = ReadTripnoteListFromDB(userId=userId)
    result = []
    Tripnote(id=1, name='Test1', dest="광화문`126512~종묘 [유네스코 세계문화유산]`126510~인사동`264353~",
             cat="관광지~관광지~관광지~").save()
    Tripnote(id=2, name="Test2",
             dest="종로~혜화~대학로~", cat="관광지~관광지~관광지~").save()
    result = Tripnote.objects.filter()
    retItems = {}
    i = 0
    for item in result:
        items = item.name
        retItems['item'+str(i)] = items
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
        name = request.POST.get("name", "")
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

        tripNotes = Tripnote.objects.filter(name=name)
        retItems = {}

        i = 0
        dests = []
        cats = []
        codes = []
        for tripNote in tripNotes:
            # dests_codes = tripNote.dest.split('~')
            dests = tripNote.dest.split('~')
            cats = tripNote.cat.split('~')

            for dest,   cat in zip(dests,   cats):
                category = []
                category = DurumiCat.objects.filter(durumiDesc=cat)

                for c in category:
                    cat_ = c.iconAddr

                    d = dest.split('`')
                    dest_ = d[0]
                    code_ = d[1]
                # cat = "/static/image/icons/13.png"

                place = json.loads(sa.codeFindAPI(code_)['item0'])

                item = {}

                item['cat'] = cat_
                item['dest'] = dest_
                item['code'] = code_
                item['mapx'] = str(place['mapx'])
                item['mapy'] = str(place['mapy'])
                #item['mapy'] = place['item0'].mapy
                #item['place'] = place

                retItems['item'+str(i)] = item
                i += 1

        context = {
            "Test": request.POST.get("name", ""),
            "result": retItems
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
