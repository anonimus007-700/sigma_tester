from django.shortcuts import render

from .models import *
from .forms import TestsForm, QuestionForm, AnswerForm, Multiform

def tests(request):
    multiform = Multiform(answer_fields=4, question_fields=1)

    if request.method == "POST":
        test_form = TestsForm(request.POST)
        question_form = multiform.QuestionFormSet(request.POST)
        answer_form = multiform.AnswerFormSet(request.POST)
        
        if 'add' in request.POST:
             multiform = Multiform(answer_fields=12, question_fields=3)

        if (answer_form.is_valid() and
            test_form.is_valid() and
            question_form.is_valid()):

            tests = Tests.objects.create(author=request.user,
                                         name=test_form['name'].value())
            question = Question.objects.create(test=tests,
                                               question_text=question_form['question_text'].value())
            for i in answer_form.cleaned_data:
                answer = Answer.objects.create(question=question,
                                               answer_text=i['answer_text'],
                                               istrue=i['is_true'])
            
            # tests.save()
            # question.save()
            # answer.save()

    return render(request, 'content/tests.html', {'test_form': TestsForm,
                                                  'question_form': multiform.QuestionFormSet,
                                                  'answer_form': multiform.AnswerFormSet,
                                                  'x': 0})
