from django.forms import ModelForm, TextInput

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

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'istrue']

        widgets = {
            'answer_text': TextInput(attrs={
                'placeholder': 'Текст відповіді'
            }),
            'istrue': TextInput(attrs={
                'type': 'radio',
                'value': 'Чи вірно'
            }),
        }
