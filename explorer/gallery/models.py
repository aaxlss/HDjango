# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    pub_date = models.DateTimeField('date published')
    url_image = models.CharField(max_length=5000)
    description = models.CharField(max_length=320)

    def __str__(self):
        return self.description


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=320)

    def __str__(self):
        return self.content