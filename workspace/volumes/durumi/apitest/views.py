#-*- coding:utf-8 -*-
#apitest/views.py

from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse,reverse_lazy
from django.views import generic
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request

#from keyword import *

from apitest.forms import ContactForm

ServiceKey = "0Uy%2BxurbDkET33KiC3fms09%2BMzmVPuCNUMwrjsCfai8CHp%2FT%2FD0MlSoaaXB8IOZjCc9S6WzmwQuzsrnNymJmzQ%3D%3D"

# Create your views here.
def keyFind(inputKeyword):
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword'
    queryParams = '?' + 'ServiceKey='+ServiceKey+'&'+urlencode({ 
        quote_plus('MobileApp') : 'AppTest', 
        quote_plus('MobileOS') : 'ETC', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', 
        quote_plus('listYN') : 'Y', quote_plus('arrange') : 'A', quote_plus('contentTypeId') : '12', 
        quote_plus('areaCode') : '', quote_plus('sigunguCode') : '', quote_plus('cat1') : '', 
        quote_plus('cat2') : '', quote_plus('cat3') : '', quote_plus('keyword') : inputKeyword 
    })
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    return (response_body)


class IndexView(generic.ListView):
    template_name = 'apitest/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return HttpResponse("Hello, world. You're at the apitest index.")

class ContactView(generic.FormView): #contact
    template_name = 'apitest/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("apitest:formtest") #moving url when FORM request success.
 
    def form_valid(self,form):
        name = form.data.get('name')
        name2 = form.clean()
        return super().form_valid(form)
 
class FormView(generic.View): #formtest
    template_name = 'apitest/contact.html'
    form_class = ContactForm
    #success_url = reverse_lazy("apitest:contact")
    
    def post(self,request):
        inputkw = request.POST.get('name')
        result = keyFind(inputkw)
        context ={
            'result' : result
        }
        return render(request,self.template_name,context)
        
    def get(self,request):
        result = request.GET
        context ={
            'result' : result
        }
        return render(request,self.template_name,context)
    

def testView(request):   #testview
    test = reverse("apitest:formtest")
    return HttpResponse("reverse return is %s"%request.POST)
    
