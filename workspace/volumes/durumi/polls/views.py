from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import User


#유저를 예시로 사용

#DB에 튜플 삽입, save 함수 사용. 
def InsertUser(userId, userPw, introduce, linkId):
    User(userId=userId, userPw=userPw, introduce=introduce, linkId=linkId).save()
    

    #return render문과 같이 사용하여 응답 페이지 렌더링 가능
    
    #EX)
    #return render(request, 'polls/user.html', {'response_text': 'insert user' + userId })


def ShowUser(request, userId):
    result = User.objects.filter(userId=userId)[0] #userId로 검색한 첫 번째 튜플

    #아래와 같이 튜플에서 여러 필드를 선택하여 저장 가능
    userInfo = "userId: {0}; introduce: {1};".format(result.userId, result.introduce)

    #마찬가지로 return render문과 같이 사용하여 응답 페이지 렌더링 가능
    
    #EX)
    #return render(request, 'polls/user.html', {'response_text': userInfo })
