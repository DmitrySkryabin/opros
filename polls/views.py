from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.forms import modelformset_factory, inlineformset_factory, formset_factory, modelform_factory


from .forms import QuestionForm, QuestionGroupForm
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
    parent_data = Question_group.objects.all()
    for item in parent_data:
        if item.active == True:
            title = item.title
    data = Question.objects.filter(question_group_id__active=True)
    print(data)
    args={
        'data':data,
        'parent_data':parent_data,
        'title':title
    }
    return render(request, "polls/admin.html",args)

def update(request, question_id):
    args = {

    }
    return render(request, "polls/createpoll.html", args)


def create(request):
    args={}
    args['create'] = 'true'
    form_q = modelformset_factory(Question, form = QuestionForm, can_delete=True, extra=3)
    formset = form_q(queryset=Question.objects.none())
    if request.method == 'POST':
        form = QuestionGroupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("1")
                new_q = form.instance
                formq = form_q(request.POST)
                if formq.is_valid():
                    instances = formq.save(commit=False)
                    print(instances)
                    print("2")
                    for instance in instances:
                        instance.question_group_id = new_q
                        instance.save()
                    for obj in formq.deleted_objects:
                        obj.delete()
            except:
                pass
                #args['save_error']=str(e)
                #return  render(request, 'polls/createpoll.html', args)
        return redirect("polls:admin_page")
    return render(request, 'polls/createpoll.html', {
        'form': QuestionGroupForm(),
        'formset': formset,
        'create': 'create'
        })
