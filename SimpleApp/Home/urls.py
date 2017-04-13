# Home/urls.py

from django.conf.urls import url
from Home import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),  # This is home page, HomePageView.as_view() is defined inside views.py
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route, views.AboutPageView.as_view() is defined inside the views.py
]
