from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime

# Create your views here.
# this function takes a parameter request which is an object that has information about the request from user that triggered the views

def index(request):
	return HttpResponse('<html><body>Hello,World!</body></html>')

def about(request):
	return HttpResponse("here is the about page. Want to return home? <a href='/'>Back Home</a>")

def better(request):
	t = loader.get_template('betterhello.html')
	c = Context({'current_time': datetime.now(), })
	return HttpResponse(t.render(c))