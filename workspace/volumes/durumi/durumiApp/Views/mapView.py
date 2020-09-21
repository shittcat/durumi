from .. import appkey
from ..Models import MapModel
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..apicodes import searchAPI as sa
from ..Models.UserModel import User
import simplejson as json
import os
import sys

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ..Models import MapModel
from . import appkey

def mapView(request):  # 맵 템플릿 연결
    template_name = 'durumiApp/Map.html'
    # Map.html을 띄워줌
    context = {
        "Map": MapModel.Map(),
        "Appkey": appkey.Appkey

    }
    return render(request, template_name, context)


@csrf_exempt  # 보안문제로 적어줌
def searchKeyword(request):  # 해당 장소에 대한 좌표정보 전송
    template_name = 'durumiApp/Map.html'
    try:
        # searchbox에서 내용 받아와 keyword 함수 실행 하여 검색결과 JSON으로 받아옴.
        Input_str = request.POST.get("searchBox", "")
    except (KeyError, Input_str == ""):
        context = {
            "Map": MapModel.Map,
            "Appkey": appkey.Appkey
        }
        return render(request, template_name, context)
    else:
        result = sa.keywordFindAPI(Input_str)
        context = {
            "Test": Input_str,
            "result": result
        }
        return HttpResponse(json.dumps(context), content_type="application/json")


def searchLocation(request):
	try:
		Input_str = request.POST.get("gpsLoc", "") # searchbox에서 내용 받아와 keyword 함수 실행 하여 검색결과 JSON으로 받아옴. 
		code = request.POST.get("code", "") 
	except (KeyError, Input_str == "", code == ""):
		context = {
			"Map": MapModel.Map, 
			"Appkey": appkey.Appkey
		}
		return render(request,template_name,context)
	else:
		result = sa.locationFindAPI(Input_str, code)
		context = {
			"result" : result
		}
		return HttpResponse(json.dumps(context), content_type="application/json") 
