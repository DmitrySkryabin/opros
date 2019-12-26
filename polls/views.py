from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Question_group

hiden=[]
count_q=[]
class IndexView(generic.ListView):
    template_name = 'polls/main.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question_group.objects.filter(active=True).order_by('-title')

'''
class DetailView(generic.DetailView):
    model = Question.objects.filter(id=1)
    template_name = 'polls/detail.html'
'''
def detailview(request,pk):
    data = Question.objects.filter(question_group_id=pk)
    hiden.clear()
    count_q.append(len(data))
    print(count_q)
    args={
        'data':data
    }
    return render(request, 'polls/detail.html',args)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    q_id=question.question_group_id.id
    print("dfdf")
    print(q_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "ВЫ НЕ ПРОГОЛОСОВАЛИ",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #return HttpResponseRedirect(reverse('polls:detail', args=(q_id,)))
        data = Question.objects.filter(question_group_id=q_id)
        #hiden=[]
        hiden.append(question_id)
        print(count_q)
        if len(hiden) == count_q[-1]:
            args={
                'data':data,
                'hiden':hiden,
                'end':True
            }
            count_q.clear()
        else:
            args={
                'data':data,
                'hiden':hiden
            }
        print(hiden)
        return render(request, 'polls/detail.html',args)


def adminview(request):
    data = Question.objects.filter(question_group_id__active=True)
    print(data)
    args={
        'data':data
    }
    return render(request, "polls/admin.html",args)
