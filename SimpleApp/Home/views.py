from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse


import docker 


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
	client = docker.from_env()

	text = "This is simple text"
	 
	print "Number of the images are : "+ str(len(client.images.list()))
	print client.images.list()[0]
	#return HttpResponse(text)
	return HttpResponse(text)
        #return render(request, 'index.html', context=None)  comment: we can response using render also

#Add another view for new page
class AboutPageView(TemplateView):
    template_name = "about.html"


