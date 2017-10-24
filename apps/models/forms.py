# django
from django import forms
from django.contrib.contenttypes.forms import generic_inlineformset_factory
# project
from . import models

class ImageForm(forms.ModelForm):
    """ Form to create Images """

    class Meta:
        model  = models.Image
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    """ Form to create Projects """

    class Meta:
        model  = models.Project
        fields = '__all__'

""" Image formset to be included in ModelForms """
ImageFormSet = generic_inlineformset_factory(models.Image, extra=1)
