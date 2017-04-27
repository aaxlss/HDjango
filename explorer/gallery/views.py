# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.shortcuts import render
from django.template.loader import render_to_string

from django.template import loader
from django.shortcuts import redirect

from .models import Post

def home (request):
    return render(request, 'main.html')

def index(request):
    posts = Post.objects.order_by('-pub_date')
    params = {
        'posts': posts
    }
    html = render_to_string('gallery/index.html', params)
    return HttpResponse(html);
    # return redirect('redirect/', request) #showing a template calling another method
    # return render_to_string('gallery/index.html', params)
    # if request.is_ajax():
    #
    #
    # else:
    #     template = loader.get_template('gallery/index.html')
    #
    #     # return HttpResponse('<h1>hola mundo</h1>') // return html code to user
    #     return HttpResponse(template.render(params, request)); // return a template to user
    #     # return render(request, 'gallery/index.html', params) // return a template to user

def methodRedirect(request):
    posts = Post.objects.order_by('-pub_date')
    params = {
        'posts': posts
    }
    template = loader.get_template('gallery/index.html')
    return HttpResponse(template.render(params, request))