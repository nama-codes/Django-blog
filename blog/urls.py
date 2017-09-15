from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^c(?P<category_id>[0-9]+)/$',views.c_detail,name='c_detail'),
    url(r'^b(?P<blog_id>[0-9]+)/$',views.b_detail,name='b_detail'),
]
