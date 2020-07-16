from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from .Views import MapView

# Create your views here.


# def ajax(request):
#    #ajax 테스트를 위한 view
#    example = 'hello AJAX!'
#    hi = 'hi AJAX!'
#    context = { 'hello' : example,
#                'hi' : hi  }
#    return HttpResponse(json.dumps(context), content_type="application/json")


def MapView(request):
    MapView.MapView(request)


@csrf_exempt  # 보안문제로 적어줌
def Pos(request):
    MapView.Pos(request)
