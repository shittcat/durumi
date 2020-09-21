from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen, Request
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


@csrf_exempt  # 보안문제로 적어줌
