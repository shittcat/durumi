from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..apicodes import keyword
import simplejson as json
import os
import sys

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def signup(request):
    template_name = 'durumiApp/viewpage/viewSignup.html'
    data = request.POST
    if User.objects.filter(user_id= data['id']).exists():
        context = {
            "result" : "이미 존재하는 아이디입니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    else :
        User.objects.create(
            user_id = data['id'] , 
            email = data['email'] ,
            password = data['password'],
        ).save()
        context = {
            "result" : "회원가입 성공"
        }
        return HttpResponse(json.dumps(context),content_type="application/json")

@csrf_exempt
def loginCheck(request):
    template_name = 'durumiApp/loginPage.html'
    request.session['loginOk'] = False
    try:
        data = request.POST
        inputId = data['id']
        inputPW = data['password']
    except (KeyError,inputId == "",inputPassword == "") :
        context = {
            "uid" : "empty",
            "upw" : "empty",
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    
    if( (inputId == "hello") and (inputPW == "world")):
        request.session['loginOk'] = True
        context = {
            "result" : "로그인 성공"
        }
    else :
        request.session['loginOk'] = False
        context = {
            "result" : "비밀번호가 틀렸습니다"
        }
    return HttpResponse(json.dumps(context),content_type="application/json")
    # else : 
    #     if User.objects.filter(user_id= inputId).exists():
    #         getUser = User.objects.get(user_id = inputId)
    #         if getUser.password == inputPassword : 
    #             request.session['loginOk'] = True
    #             context = {
    #                 "result" : "로그인 성공"
    #             }
    #         else :
    #             request.session['loginOk'] = False
    #             context = {
    #                 "result" : "비밀번호가 틀렸습니다"
    #             }
    #     else :
    #         request.session['loginOk'] = False
    #         context = {
    #             "result" : "존재하지 않는 id입니다"
    #         }
    #     return HttpResponse(json.dumps(context),content_type="application/json")

@csrf_exempt
def loginOk(request):
    template_name = 'durumiApp/loginPage.html'
    if request.session['loginOk'] == True :
        context = {
            "ok" : "True"
        }
    else :  
        context = {
            "ok" : "False"
        }
    return HttpResponse(json.dumps(context),content_type="application/json")

@csrf_exempt    
def logOut(request):
    request.session['loginOk'] = False
    
    return HttpResponse("",content_type="application/json")