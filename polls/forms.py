from django import forms

from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)

class QuestionGroupForm(forms.ModelForm):
    class Meta:
        model = Question_group
        fields = ('title',)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)
