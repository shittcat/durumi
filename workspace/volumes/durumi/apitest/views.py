#-*- coding:utf-8 -*-
#apitest/views.py

from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
from .apicodes import keyword
#from keyword import *
from .apicodes import MapView

from apitest.forms import ContactForm

# Create your views here.
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
    
    def get(self, request):
        return render(request,self.template_name)

    def post(self,request):
        inputkw = request.POST.get('name')
        result = keyword.keywordFindAPI(inputkw)
        context ={
            'result' : result
        }
        return render(request,self.template_name,context)

def testView(request):   #testview
    test = reverse("apitest:formtest")
    return HttpResponse("reverse return is %s"%request.POST)
    
def MapView(request):
    MapView.MapView(request)

@csrf_exempt  # 보안문제로 적어줌
def Pos(request):
    MapView.Pos(request)
