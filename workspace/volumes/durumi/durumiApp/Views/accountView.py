from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..apicodes import keyword
from ..Models.UserModel import User
import simplejson as json
import os
import sys

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#유저를 예시로 사용

#DB에 튜플 삽입, save 함수 사용. 
def InsertUser(userId, userPw, introduce, linkId):
    User(userId=userId, userPw=userPw, introduce=introduce, linkId=linkId).save()

    #return render문과 같이 사용하여 응답 페이지 렌더링 가능
    
    #EX)
    #return render(request, 'polls/user.html', {'response_text': 'insert user' + userId })


def ShowUser(request, userId):
    result = User.object.filter(userId=userId)[0] #userId로 검색한 첫 번째 튜플
    #아래와 같이 튜플에서 여러 필드를 선택하여 저장 가능
    userInfo = "userId: {0}; introduce: {1};".format(result.userId, result.introduce)

    #마찬가지로 return render문과 같이 사용하여 응답 페이지 렌더링 가능
    
    #EX)
    #return render(request, 'polls/user.html', {'response_text': userInfo })

@csrf_exempt
def signup(request):
    template_name = 'durumiApp/viewpage/viewSignup.html'
    data = request.POST
    if User.objects.filter(userId= data['id']).exists():
        context = {
            "result" : "이미 존재하는 아이디입니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    else :
        User(
            userId = data['id'] , 
            userPw= data['pw'],
            introduce = data['introduce'] ,
            linkId = "none" ,
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
        return HttpResponse(content_type="application/json")
    
    if User.objects.filter(userId= data['id']).exists():
        result = User.objects.filter(userId=inputId)[0] #userId로 검색한 첫 번째 튜플
        userInfo = "userId: {0}; introduce: {1};".format(result.userId, result.userPw)
        if( (inputId == result.userId) and (inputPW == result.userPw)):
            request.session['loginOk'] = True
            context = {
                "result" : "로그인 성공"
            }
        else :
            request.session['loginOk'] = False
            context = {
                "result" : "비밀번호가 틀렸습니다"
        }
    else :
        request.session['loginOk'] = False
        context = {
            "result" : "존재하지 않는 ID입니다."
        }
    return HttpResponse(content_type="application/json")
    
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