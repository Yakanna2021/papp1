from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

'''def index(request):
    return render(request,'home.html')'''

class AboutPageView(TemplateView):
    template_name = "about.html"
    