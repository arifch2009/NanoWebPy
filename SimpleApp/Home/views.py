from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse


import docker 


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
	client = docker.from_env()

	container_text =  "Numner of containers running in this machine : "+ str(len(client.containers.list())) + "<br>Container details : <table border: 1px ><tr><th>Name </th><th>Container ID</th></tr>"
        for i in client.containers.list():
		container_text= container_text + "<tr><td>"+ i.name +   "</td><td>"+ i.id[0:10] + "</td></tr>"


        container_text= container_text +"</table>"
	
        
	image_text =  "Numner of images in this machine : "+ str(len(client.images.list())) + "<br> Detail of the images are : <table border: 1px ><tr><th>Image id</th></tr>"
        for i in client.images.list():
		if i.id.startswith('sha256:'):
			image_text= image_text + "<tr><td><a href=''> " + i.id[7:17] + " </a></td></tr>"


        image_text= image_text +"</table>"

	
	#return HttpResponse(text)
	return HttpResponse(container_text+ image_text)
        #return render(request, 'index.html', context=None)  comment: we can response using render also

#Add another view for new page
class AboutPageView(TemplateView):
    template_name = "about.html"


