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

def hola(request):
    return HttpResponse('<h1>hola mundo</h1>')

def index(request):
    posts = Post.objects.order_by('-pub_date')

    params = {
        'posts': posts,
        'father': '',
    }

    if request.is_ajax():#if is a ajax request render without father template
        html = render_to_string('gallery/index.html', params)
        return HttpResponse(html)

    else:#render with father template
        params ['father'] = 'main.html'
        template = loader.get_template('gallery/index.html')
        return render(request, 'gallery/index.html', params)

    # return redirect('redirect/', request) #showing a template calling another method
    # return render_to_string('gallery/index.html', params)
    #
    #
    #
    # else:
    #     template = loader.get_template('gallery/index.html')
    #
    #     # return HttpResponse('<h1>hola mundo</h1>') // return html code to user
    #     return render(request, 'gallery/index.html', params)


def redirectMethod (request):
    return redirect('/gallery/render-redirect')  # showing a template calling another method

def methodRedirect(request):
    posts = Post.objects.order_by('-pub_date')
    params = {
        'posts': posts,
        'father': 'main.html',
    }
    template = loader.get_template('gallery/index.html')
    return HttpResponse(template.render(params, request))