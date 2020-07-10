from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from . import keyword
import simplejson as json
import os
import sys

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ..Models import MapModel
from .. import appkey


def MapView(request):
	template_name = 'apitest/Map.html'
	# Map.html을 띄워줌
	context = {
		"Map": MapModel.Map(), 
		"Appkey": appkey.Appkey
	}
	return render(request,template_name,context)


@csrf_exempt  # 보안문제로 적어줌
def Pos(request):
	template_name = 'apitest/Map.html'
	try:
		Input_str = request.POST.get("searchBox", "")
	except (KeyError, Input_str == ""):
		context = {
			"Map": MapModel.Map, 
			"Appkey": appkey.Appkey
		}
		return render(request,template_name,context)
	else:
		result = keyword.keywordFindAPI(Input_str)
		context = {
			"result" : result
		}
		# Input = Input_str
		# map = MapModel.Map()
		# Pos = getPos(Input)
		# map.moveLocation(Pos[0], Pos[1])
		# # context를 HTML파일로 보내줌
		# context = {
		# 	"Input": Input,
		# 	"xPos": map.xPos,
		# 	"yPos": map.yPos,
		# }
		return HttpResponse(json.dumps(context), content_type="application/json")


def getPos(Input_str):
    if Input_str == "우리집":
        return 37.49427475898042, 126.78703753036896
    if Input_str == "학교":
        return 37.48625412871462, 126.8016009357299
    if Input_str == "myhome":
        return 37.49427475898042, 126.78703753036896

    return 33.450701, 126.570667