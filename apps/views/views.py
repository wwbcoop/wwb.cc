# django
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
# project
from apps.models import models

class FrontView(View):
    """ Frontpage """

    def get(self, request):
        featured = models.Project.objects.filter(published=True, featured=True).order_by('?')
        return render(request, 'pages/front.html', locals())

class ProjectsView(ListView):
    """ List of projects """

    model = models.Project

    def get_queryset(self):
        return models.Project.objects.filter(published=True).order_by('-end_date')

class ProjectView(DetailView):
    """ View of single project """

    model = models.Project
