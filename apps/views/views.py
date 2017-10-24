# django
from django.shortcuts import render
from django.views import View

class FrontView(View):
    """ Frontpage """

    def get(self, request):
        return render(request, 'pages/front.html', locals())
