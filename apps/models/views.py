# django
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# project
from . import models, forms

modelform_generic_template = 'pages/modelform.html'

class ProjectCreate(LoginRequiredMixin, CreateView):
    """ View to display a form to create a project """

    model            = models.Project
    form_class       = forms.ProjectForm
    template_name    = modelform_generic_template
    title            = _('Añade un proyecto')

    def get_context_data(self, **kwargs):
      context                     = super(ProjectCreate, self).get_context_data(**kwargs)
      context['submit_text']      = _('Guarda el proyecto')
      context['form__html_class'] = 'project'
      return context

    def form_valid(self, form):
        messages.success(self.request, _('Proyecto creado con éxito'))
        return super(ProjectCreate, self).form_valid(form)

class ProjectEdit(LoginRequiredMixin, UpdateView):
    """ View to display a form to create a project """

    model = models.Project
    fields = '__all__'

class ProjectDelete(LoginRequiredMixin, DeleteView):
    """ View to display a form to create a project """

    model = models.Project
    fields = '__all__'
