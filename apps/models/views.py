# django
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse

# project
from . import models, forms

modelform_generic_template = 'pages/modelform.html'

class ProjectCreate(LoginRequiredMixin, CreateView):
    """ View to display a form to create a project """

    model         = models.Project
    form_class    = forms.ProjectForm
    template_name = modelform_generic_template
    success_url   = reverse_lazy('front')

    def get_context_data(self, **kwargs):
        context                     = super(ProjectCreate, self).get_context_data(**kwargs)
        context['title']            = _('Añade un proyecto')
        context['submit_text']      = _('Guarda el proyecto')
        context['form__html_class'] = 'project'

        if self.request.POST:
            context['images']  = forms.ImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['images']  = forms.ImageFormSet(instance=models.Project())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        if images.is_valid():
            self.object = form.save()
            images.instance = self.object
            images.save()
            messages.success(self.request, _('Proyecto creado con éxito'))
            return super(ProjectCreate, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ProjectEdit(LoginRequiredMixin, UpdateView):
    """ View to display a form to create a project """

    model = models.Project
    form_class    = forms.ProjectForm
    template_name = modelform_generic_template
    title         = _('Edita el proyecto')
    success_url   = reverse_lazy('front')

    def get_context_data(self, **kwargs):
      context                     = super(ProjectEdit, self).get_context_data(**kwargs)
      context['submit_text']      = _('Guarda los cambios')
      context['form__html_class'] = 'project'
      pk                          = self.kwargs['pk']
      if self.request.POST:
        context['images'] = forms.ProjectImageFormSet(self.request.POST)
      else:
        context['images'] = forms.ProjectImageFormSet(instance=models.Project.objects.get(pk=pk))
      return context

class ProjectDelete(LoginRequiredMixin, DeleteView):
    """ View to display a form to create a project """

    model = models.Project
    fields = '__all__'
