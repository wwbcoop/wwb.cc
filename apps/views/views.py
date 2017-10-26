# django
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
# project
from apps.models import models

class FrontView(View):
    """ Frontpage """

    def get(self, request):
        return render(request, 'pages/front.html', locals())

class ProjectsView(ListView):
    """ List of projects """

    model = models.Project

class ProjectView(DetailView):
    """ View of single project """

    model = models.Project
