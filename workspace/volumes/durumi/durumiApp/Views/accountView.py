from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from ..apicodes import keyword
from ..Models.UserModel import User
import simplejson as json
import os
import sys
import bcrypt

# 상위폴더의 파일을 import 하기 위해 상위폴더의 Path를 등록해줌
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

@csrf_exempt
def signup(request):
    template_name = 'durumiApp/viewpage/viewSignup.html'
    data = request.POST
    if User.objects.filter(userId=data['id']).exists():
        context = {
            "result": "이미 존재하는 아이디입니다."
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        # bcrypt는 bytes형식만 사용
        # 입력받은 str 형식의 PW를 bytes형식으로 인코딩
        input_pw = data['pw'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(input_pw, salt)

        # DB저장을 위해 bytes->str 형변환
        decoded_salt = salt.decode('utf-8')
        decoded_pw = hashed_pw.decode('utf-8')

        User(
            userId = data['id'] , 
            userPw = decoded_pw,
            userSalt = decoded_salt,
            linkId = data['id']
        ).save()
        context = {
            "result": "회원가입 성공"
        }
        return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def loginCheck(request):
    template_name = 'durumiApp/loginPage.html'
    request.session['loginOk'] = False
    try:
        data = request.POST
        inputId = data['id']
        inputPW = data['password']
    except (KeyError, inputId == "", inputPW == ""):
        context = {
            "uid": "empty",
            "upw": "empty",
        }
        return HttpResponse(json.dumps(context), content_type="application/json")

    if User.objects.filter(userId=data['id']).exists():
        result = User.objects.filter(userId=inputId)[0]  # userId로 검색한 첫 번째 튜플

        # DB에서 가져온 소금값을 str에서 bytes로 형변환
        encoded_salt = result.userSalt.encode('utf-8')

        # 입력받은 PW를 bytes형식으로 바꾸고 해싱
        encoded_pw = inputPW.encode('utf-8')
        inputPW = bcrypt.hashpw(encoded_pw, encoded_salt)

        # DB에서 가져온 해싱된 PW를 str에서 bytes로 형변환
        userPw = result.userPw.encode('utf-8')

        if((inputId == result.userId) and (inputPW == userPw)):
            request.session['loginOk'] = True
            request.session['userId'] = inputId
            context = {
                "result" : "ok"
            }
        else:
            request.session['loginOk'] = False
            context = {
                "result" : "로그인 실패. 비밀번호가 틀렸거나 존재하지 않는 ID입니다."
        }
    else :
        request.session['loginOk'] = False
        context = {
            "result" : "로그인 실패. 비밀번호가 틀렸거나 존재하지 않는 ID입니다."
        }
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def loginOk(request):
    template_name = 'durumiApp/loginPage.html'
    if request.session['loginOk'] == True:
        context = {
            "ok": "True"
        }
    else:
        context = {
            "ok": "False"
        }
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def logOut(request):
    request.session['loginOk'] = False
    request.session['userId'] = ""
    return HttpResponse("",content_type="application/json")
