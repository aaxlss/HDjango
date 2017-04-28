from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hola-mundo/', views.hola, name = 'holaMundo'),
    url(r'^redirect/$', views.redirectMethod, name = 'render-redirect'),
    url(r'^render-redirect/$', views.methodRedirect, name='render'),
    url(r'^$', views.index, name = 'index'),
]