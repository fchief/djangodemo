from django.conf.urls import url, include
from django.contrib import admin
from .views import PostView, delete_post

urlpatterns = [
    url(r'^(?P<id>\d+)/$', PostView.as_view(template_name='post.html'), name="update_post"),
    url(r'^$', PostView.as_view(template_name='post.html'), name="post"),
    url(r'^(?P<id>\d+)/delete/$', delete_post, {'template_name' : 'delete.html'}, name="delete"),
]
