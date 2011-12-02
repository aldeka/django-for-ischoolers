from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from qandabear.models import Question

def index(request):
    latest_qs = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_qs': latest_qs}
    return render_to_response('qandabear/index.html', context)
    
def question(request, question_id):
    try:
        q = Question.objects.get(id=question_id)
    except:
        raise Http404
    return render_to_response('qandabear/detail.html', {'question':  q})
    
def edit_answer(request, question_id, answer_id):
    return HttpResponse("You're looking at the edit page for answer %s." % (answer_id,))
