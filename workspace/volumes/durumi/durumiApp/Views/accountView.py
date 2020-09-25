from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from ..apicodes import keyword
from ..Models.UserModel import User
import simplejson as json
import os
import sys
import bcrypt
import string
import random

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
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif len(data['pw']) < 8:
        context = {
            "result" : "비밀번호는 8글자 이상이어야 합니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif data['pw'] != data['pwcheck'] :
        context = {
            "result" : "비밀번호가 일치하지 않습니다"
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif data['pw'].isdigit():
        context = {
            "result" : "비밀번호에 문자를 포함해주시기 바랍니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif '@' not in data['email']:
        context = {
            "result" : "올바른 이메일 형식이 아닙니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")\
        
    #bcrypt는 bytes형식만 사용
    #입력받은 str 형식의 PW를 bytes형식으로 인코딩
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
        linkId = data['id'],
        userMail = data['email'],
    ).save()
    context = {
        "result": "ok"
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def findPW(request):
    template_name = 'durumiApp/viewpage/viewFindPW.html'
    data = request.POST
    if not User.objects.filter(userId= data['id']).exists():
        context = {
            "result" : "존재하지 않는 아이디 입니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif '@' not in data['email']:
        context = {
            "result" : "올바른 이메일 형식이 아닙니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    else :
        input_mail = data['email']
        result = User.objects.filter(userId=data['id'])[0] #userId로 검색한 첫 번째 튜플

        if(result.userMail != input_mail):
            context = {
                "result" : "등록된 메일이 아닙니다."
            }
            return HttpResponse(json.dumps(context),content_type="application/json")
        else:
            #무작위 비밀번호 생성
            string_pool = string.ascii_letters + string.digits
            new_Pw = ""
            for i in range(10):
                new_Pw += random.choice(string_pool)

            #메일 데이터 생성
            new_subject = '초기화된 비밀번호 입니다.'
            new_message = new_Pw + '로 접속하시기 바랍니다.'
            #mail = EmailMessage(subject, message, to=[input_mail])

            #메일 전송
            #mail.send()
            send_mail(
                subject = new_subject,
                message = new_message,
                from_email = None,
                recipient_list = [input_mail],
                fail_silently = False
            )
            
            #비밀번호 해싱 및 형변환
            new_Pw = new_Pw.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed_pw = bcrypt.hashpw(new_Pw, salt)
            decoded_salt = salt.decode('utf-8')
            decoded_pw = hashed_pw.decode('utf-8')

            result.userSalt = decoded_salt
            result.userPw = decoded_pw
            result.save()
            
            context = {
                "result" : "ok"
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

@csrf_exempt
def loadInfo(request):
    sessionId = request.session['userId']
    result = User.objects.filter(userId=sessionId)[0]  # userId로 검색한 첫 번째 튜플
    
    email = result.userMail
    introduce = result.introduce

    context = {
        "mail": email,
        "introduce": introduce
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def changeInfo(request):
    template_name = 'durumiApp/viewpage/viewInfo.html'
    data = request.POST
    sessionId = request.session['userId']
    if (data['email'] != "") and ('@' not in data['email']):
        context = {
            "result" : "올바른 이메일 형식이 아닙니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")\
    
    result = User.objects.filter(userId=sessionId)[0] #userId로 검색한 첫 번째 튜플
    
    #!!후일 viewInfo 수정으로 디폴트값 출력시 함수 변경 필요
    if(data['email'] != ""):
        result.userMail = data['email']

    if(data['introduce'] != ""):
        result.introduce = data['introduce']

    result.save()

    context = {
        "result": "ok"
    }
    return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def changePw(request):
    template_name = 'durumiApp/viewpage/viewChangePw.html'
    data = request.POST
    if  data['pw'] == "":
        context = {
            "result" : "비밀번호를 입력해주세요."
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    elif len(data['pw']) < 8:
        context = {
            "result" : "비밀번호는 8글자 이상이어야 합니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif data['pw'] != data['pwcheck'] :
        context = {
            "result" : "비밀번호가 일치하지 않습니다"
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif data['pw'].isdigit():
        context = {
            "result" : "비밀번호에 문자를 포함해주시기 바랍니다."
        }
        return HttpResponse(json.dumps(context),content_type="application/json")
    else:
        sessionId = request.session['userId']
        inputPw = data['pw']
        result = User.objects.filter(userId=sessionId)[0] #userId로 검색한 첫 번째 튜플

        #bcrypt는 bytes형식만 사용
        #입력받은 str 형식의 PW를 bytes형식으로 인코딩
        inputPw = inputPw.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(inputPw, salt)

        # DB저장을 위해 bytes->str 형변환
        decoded_pw = hashed_pw.decode('utf-8')
        decoded_salt = salt.decode('utf-8')

        result.userPw = decoded_pw
        result.userSalt = decoded_salt
        result.save()

        context = {
            "result": "ok"
        }

        return HttpResponse(json.dumps(context), content_type="application/json")