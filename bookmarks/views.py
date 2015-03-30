# -*- coding: utf-8 -*-

# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
	template = get_template('main_page.html')
	variables = Context({
		'head_title': 'django bookmark',
		'page_title': 'welcome to django bookmark',
		'page_body': 'share and add to bookmarks',
		})
	output = template.render(variables)
	return HttpResponse(output)
