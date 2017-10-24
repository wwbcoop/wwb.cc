# django
from django import forms
from django.contrib.contenttypes.forms import generic_inlineformset_factory
# project
from . import models
from apps.utils import widgets

class ImageForm(forms.ModelForm):
    """ Form to create Images """

    class Meta:
        model  = models.Image
        fields = '__all__'
        widgets = {
            'image_file' : widgets.PictureWithPreviewWidget(),
        }


class ProjectForm(forms.ModelForm):
    """ Form to create Projects """

    class Meta:
        model  = models.Project
        fields = '__all__'
    class Media:
        js = ('http://code.jquery.com/jquery-3.2.1.min.js',
              'utils/js/jquery.formset.js',)

""" Image formset to be included in ModelForms """
ImageFormSet = generic_inlineformset_factory(models.Image, extra=3, form=ImageForm)
