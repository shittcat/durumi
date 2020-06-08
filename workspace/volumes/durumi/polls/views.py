from django.shortcuts import render
from django.http import HttpResponse , Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from .forms import PosForm
from .models import Map
# Create your views here.

def main(request):
    #기본 View
    return render(request, 'polls/index.html')

#def ajax(request):
#    #ajax 테스트를 위한 view
#    example = 'hello AJAX!'
#    hi = 'hi AJAX!'
#    context = { 'hello' : example,
#                'hi' : hi  }
#    return HttpResponse(json.dumps(context), content_type="application/json")

def MapView(request):
    #Map.html을 띄워줌
    map = Map()
    return render(request, 'polls/Map.html', {'Map':map})

@csrf_exempt #보안문제로 적어줌
def Pos(request):
    try:
        #Post로 데이터를 받아옴 .get('이름', 'default)
        #Input_xPos = request.POST.get('xPos','')
        #Input_yPos = request.POST.get('yPos','')
        Input_str = request.POST.get('searchBox','')
    except (KeyError, Input_str==''):
        return render(request,'polls/SimpleMap.html')

    else:
        Input = Input_str
        map = Map()
        Pos = getPos(Input)
        map.moveLocation(Pos[0], Pos[1])
        #context를 HTML파일로 보내줌
        context = { 
                    'Input': Input,
                    'xPos' : map.xPos,
                    'yPos' : map.yPos,
                }
        return HttpResponse(json.dumps(context), content_type="application/json")

def getPos(Input_str):
    if Input_str == '우리집':
        return 37.49427475898042, 126.78703753036896
    if Input_str == '학교':
        return 37.48625412871462, 126.8016009357299
    if Input_str == 'myhome':
        return 37.49427475898042, 126.78703753036896

    return 33.450701, 126.570667




def SimpleMap(request):
      return render(request, 'polls/SimpleMap.html', {'Map':map} ) 