#polls/views.py

from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question 
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    #context = Question.objects.order_by("-pub_date")[:5]

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question

class ResultsView(generic.DetailView):
    template_name = "polls/results.html"
    model = Question

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


    
