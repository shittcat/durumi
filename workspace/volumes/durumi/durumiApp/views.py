#-*- coding:utf-8 -*-
#durumiApp/views.py

from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
from .apicodes import *

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'durumiApp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return HttpResponse("Hello, world. You're at the durumiApp index.")

def testView(request):   #testview
    test = reverse("durumiApp:formtest")
    return HttpResponse("reverse return is %s"%request.POST)