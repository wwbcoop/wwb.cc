# django
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
# project
from . import models

class ProjectCreate(CreateView):
    """ View to display a form to create a project """

    model  = models.Project
    fields = '__all__'

class ProjectEdit(UpdateView):
    """ View to display a form to create a project """

    model = models.Project
    fields = '__all__'

class ProjectDelete(DeleteView):
    """ View to display a form to create a project """

    model = models.Project
    fields = '__all__'
