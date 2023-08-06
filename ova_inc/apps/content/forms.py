from django.forms import ModelForm, Form, TextInput, BooleanField, CharField, formset_factory

from django.contrib.auth.models import User
from .models import Tests, Question, Answer

class TestsForm(ModelForm):
    class Meta:
        model = Tests
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Назва тесту'
            }),
        }

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        
        widgets = {
            'question_text': TextInput(attrs={
                'placeholder': 'Текст питання'
            }),
        }


class AnswerForm(Form):
    answer_text = CharField()
    is_true = BooleanField(required=False)


class Multiform:
    def __init__(self, answer_fields: int, question_fields: int) -> None:
        self.answer_fields = answer_fields
        self.question_fields = question_fields

        self.AnswerFormSet = formset_factory(AnswerForm, extra=self.answer_fields)
        self.QuestionFormSet = formset_factory(QuestionForm, extra=self.question_fields)
