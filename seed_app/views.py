from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse

import textwrap

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class RegisterView(TemplateView):
    def post(self, request, **kwargs):
        #name = request.POST.get('name')
        return render(request, "about.html", context=None)

class WelcomeView(TemplateView):
    def post(self, request, **kwargs):
        return render(request, "welcome.html", context=None)
