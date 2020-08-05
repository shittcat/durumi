#login/views.py
from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.views.decorators.csrf import csrf_exempt
from .models import User
# Create your views here.

def login(request):
    template_name = 'login.html'
    context = {
        "name" : 'login'
    }
    return render(request,template_name,context)
    
def base(request):
    template_name = 'base.html'
    context = {
        "name" : 'base'
    }
    return render(request,template_name,context)
    
@csrf_exempt
def signup(request):
    template_name = 'login.html'
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
    template_name = 'login.html'
    request.session['loginOk'] = False
    try:
        data = request.POST
        inputId = data['id']
        inputPassword = data['password']

    except (KeyError,inputId == "",inputPassword == "") :
        context = {
            "uid" : "empty",
            "upass" : "empty",
        }
        return render(request,template_name,context)
    else : 
        if User.objects.filter(user_id= inputId).exists():
            getUser = User.objects.get(user_id = inputId)
            if getUser.password == inputPassword : 
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
                "result" : "존재하지 않는 id입니다"
            }
        return HttpResponse(json.dumps(context),content_type="application/json")

@csrf_exempt
def loginOk(request):
    template_name = 'login.html'
    if request.session['loginOk'] == True :
        context = {
            "ok" : "True"
        }
    else :  
        context = {
            "ok" : "False"
        }
    return HttpResponse(json.dumps(context),content_type="application/json")
        