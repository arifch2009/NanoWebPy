# Home/urls.py

from django.conf.urls import url
from Home import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
