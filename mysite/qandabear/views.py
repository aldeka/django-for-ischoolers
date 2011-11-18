from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! You're on the questions index page!!!")
    
def question(request, question_id):
    return HttpResponse("You're looking at question %s." % (question_id,))
    
def edit_answer(request, question_id, answer_id):
    return HttpResponse("You're looking at the edit page for answer %s." % (answer_id,))
