from django import forms

from .models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)
        labels = {
           'question_text': 'Текст вопроса:',
           }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question_text'].widget.attrs.update({'class' : 'form-control'})


class QuestionGroupForm(forms.ModelForm):
    class Meta:
        model = Question_group
        fields = ('title',)
        labels = {
           'title': 'Название опроса:',
           }

    def __init__(self, *args, **kwargs):
        super(QuestionGroupForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)
        labels = {
           'choice_text': 'Ответ на вопрос:',
           }

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['choice_text'].widget.attrs.update({'class' : 'form-control'})
