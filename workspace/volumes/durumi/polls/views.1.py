#polls/views.py

from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from .models import Question 
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = '\n '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    context = {'latest_question_list':latest_question_list,
        'test_value':"hello test"
    }
    return render(request,'polls/index.html',context)
    
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question' : question}
    return render(request,'polls/detail.html',context)

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = { 'question' : question}
    return render(request,'polls/results.html',context)

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try : 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except : 
        context = {'question':question,
            'error_message' : "You did not select a choice"
        }
        # when fail at choice, going to detail page and show error message
        return render(request,'polls/detail.html',context)
    else :
        selected_choice.votes += 1 
        selected_choice.save() 
        #when choice successfull, return HttpResponse redirect 
    return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))


    
