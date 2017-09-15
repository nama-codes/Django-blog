# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Blog,Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'publisher')
    search_fields = ['title']
    list_filter = ['pub_date']


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
