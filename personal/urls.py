from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.homeview, name='homepage'),
    url(r'^contact$', views.contactview, name='contactpage'),
    url(r'^blog$', views.blogview, name='blogpage'),
    url(r'^blog/(?P<pk>[0-9]+)$', views.PostView.as_view(), name='postpage')
]