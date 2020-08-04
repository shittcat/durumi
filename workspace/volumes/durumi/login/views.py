#login/views.py
from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.views.decorators.csrf import csrf_exempt
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
def loginCheck(request):
    template_name = 'login.html'
    request.session['loginOk'] = False
    try:
        inputId = request.POST.get("id","")
        inputPassword = request.POST.get("password","")
    except (KeyError,inputId == "",inputPassword == "") :
        context = {
            "uid" : "empty",
            "upass" : "empty",
        }
        return render(request,template_name,context)
    else : 
        if( inputId == "hello" and inputPassword == "world") :
            request.session['loginOk'] = True
        else :
            request.session['loginOk'] = False
        context = {
            "uid" : inputId,
            "upass" : inputPassword
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
        