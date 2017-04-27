from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^redirect/$', views.methodRedirect, name = 'render'),
    url(r'^$', views.index, name = 'index'),
]