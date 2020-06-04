from django.shortcuts import render
from django.http import HttpResponse , Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from .forms import PosForm
# Create your views here.

def main(request):
    #기본 View
    return render(request, 'polls/index.html')

def ajax(request):
    #ajax 테스트를 위한 view
    example = 'hello AJAX!'
    hi = 'hi AJAX!'
    context = { 'hello' : example,
                'hi' : hi  }
    return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt #보안문제로 적어줌
def Pos(request):
    try:
        #Post로 데이터를 받아옴 .get('이름', 'default)
        Input_xPos = request.POST.get('xPos','0.0')
        Input_yPos = request.POST.get('yPos','0.0')
        
    except (KeyError, Input_xPos=="", Input_yPos==""):
        return render(request,'polls/index.html')

    else: 
        xPos = float(Input_xPos)
        yPos = float(Input_yPos)
        #context를 HTML파일로 보내줌
        context = { 'xPos' : xPos, 
                    'yPos' : yPos }
        return HttpResponse(json.dumps(context), content_type="application/json")
