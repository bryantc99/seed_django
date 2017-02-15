from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse


import textwrap

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)