# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Category, Blog

def index(request):
    category_list = Category.objects.order_by('id')[:5]
    context = {'category_list': category_list}
    return render(request, 'blog/index.html', context)

def b_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/b_detail.html', {'blog': blog,'error_message': "You didn't select a choice.",})

def c_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'blog/c_detail.html', {'category': category,'error_message': "You didn't select a choice.",})
