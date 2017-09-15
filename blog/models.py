# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Blog(models.Model):
    data = models.CharField(max_length=5000)
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    publisher = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
