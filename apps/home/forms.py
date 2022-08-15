# forms.py
from django import forms
from .models import Technology, Questions
from django.views.generic.edit import FormView


class TechForm(forms.ModelForm):

    class Meta:
        model = Technology
        fields = ['techName', 'techSubname', 'description', 'is_active', 'image']

class QuestionsForm(forms.ModelForm):

    class Meta:
        model = Questions
        fields = ['question', 'answer', 'experience', 'technology']