# django
from django import forms
from django.forms import inlineformset_factory
# project
from . import models

class ImageForm(forms.ModelForm):
    """ Form to create Images """

    class Meta:
        models = models.Image
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    """ Form to create Projects """

    class Meta:
        models = models.Project
        fields = '__all__'

""" Image formset to be included in ModelForms """
ImageFormSet = inlineformset_factory(Project, Image, form=ImageForm, extra=1)
