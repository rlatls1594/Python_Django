from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from vote.models import Question, Choice

# Create your views here.
def index(request):
  question_list = Question.objects.all().order_by()
  context = {'question_list' : question_list}
  #print(context['question_list'])
  #print(type(context['question_list'][0]))
  #print(context['question_list'][0].id)
  #print(context['question_list'][0].question_text)
  #print(context['question_list'][0].date)
  return render(request, 'vote/index.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'vote/detail.html', {'question' : question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    select_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    context = {'question':question, 'error_msg':"You didn't select a choice"}
    return render(request, 'vote/detail.html', context)
  else:
    select_choice.votes += 1
    select_choice.save()
    return HttpResponseRedirect(reverse('vote:result', args=(question.id,)))

def result(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'vote/result.html', {'question':question})