from django.conf.urls import patterns, url
from hello_world import views

# this code is used to link or map a url to ournspecific home page
urlpatterns = patterns('hello_world.views', url(r'^$', views.index, name='index'), url(r'^about/', views.about, name='about'), url(r'^better/$', views.better, name='better'))