from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from main.models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from main.forms import *
from django.contrib.auth import authenticate, login, logout
#forms

import requests
import os
import sys


# Create your views here.


def json_response(request):
	search_string = request.GET.get('search', '')
	if search_string != "":
		area_list = []
		for gov in Gov.objects.filter(name__icontains=search_string):
			area_list.append([gov.name, gov.pk, 'gov'])
		for area in Area.objects.filter(name__icontains=search_string):
			area_list.append([area.name, area.pk, 'area'])
		return JsonResponse(area_list, safe=False)
	else:
		return JsonResponse("", safe=False)

def ajax_search(request):
	context = {}
	return render_to_response('ajax_search.html', context, context_instance=RequestContext(request))

def details_view(request):
	xtype = request.GET.get('xtype', '')
	xid = request.GET.get('xid', '')
	context = {}
	model = None
	if xtype == "genre":
		model = Genre
		dic = {'genre_id':xid}
	if xtype == "album":
		model = Album
		dic = {'album_id':xid}
	if xtype == "artist":
		model = Artist
		dic = {'artist_id':xid}
	if xtype == "track":
		model = Track
		dic = {'track_id':xid}

	grabit(xtype , xid)
	try:
		xobject = model.objects.get(**dic)

	except Exception, e:
		xobject = "Failed"
	context['xtype'] = xtype
	context['xobject'] = xobject
	return render_to_response('details.html', context, context_instance=RequestContext(request))


def list_view(request):
	context = {}
	type_of_search = request.GET.get('type', None)
	search_id = request.GET.get('id', None)
	appartments = []
	if type_of_search == 'gov':
		gov = Gov.objects.get(id=search_id)

		for area in gov.area_set.all():
			for appartment in area.appartment_set.all():
				appartments.append(appartment)

		context['appartments'] = appartments

	elif type_of_search == 'area':
		area = Area.object.get(id=search_id)
		for appartment in area.appartment_set.all():
			appartments.append(appartment)
		context['appartments'] = appartments
	return render(context, 'list_view.html', request)