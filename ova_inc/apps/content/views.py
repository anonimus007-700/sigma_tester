from django.shortcuts import render

from .forms import TestsForm, QuestionForm, AnswerForm

def tests(request):
    if request.method == "POST":
        test_form = TestsForm(request.POST)
        question_form = QuestionForm(request.POST)
        answer_form = AnswerForm(request.POST)

        print(test_form['name'].value())
        print(question_form['question_text'].value())
        print(answer_form['answer_text'].value())

    return render(request, 'content/tests.html', {'test_form': TestsForm,
                                                  'question_form': QuestionForm,
                                                  'answer_form': AnswerForm})
