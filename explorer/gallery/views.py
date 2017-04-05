# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader

from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')
    params = {
        'posts': posts
    };

    template = loader.get_template('gallery/index.html')
    return render(request, 'gallery/index.html', params)