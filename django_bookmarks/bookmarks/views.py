# -*- coding: utf-8 -*-

# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

def main_page(request):
	template = get_template('main_page.html')
	variables = Context({
		'head_title': 'django bookmark',
		'page_title': 'welcome to django bookmark',
		'page_body': 'share and add to bookmarks',
		})
	output = template.render(variables)
	return HttpResponse(output)

def user_page(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('Dont search users')
	
	bookmarks = user.bookmark_set.all()
	
	template = get_template('user_page.html')
	variables = Context({
		'username': username,
		'bookmarks': bookmarks
		})
	output = template.render(variables)
	return HttpResponse(output)
