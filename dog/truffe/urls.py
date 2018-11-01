from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^posts/(?P<id>[0-9]+)$', views.show),
]
