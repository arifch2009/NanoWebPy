from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
 


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
	text = """<h1>welcome to my app !</h1>"""
	return HttpResponse(text)
        #return render(request, 'index.html', context=None)  comment: we can response using render also

#Add another view for new page
class AboutPageView(TemplateView):
    template_name = "about.html"


