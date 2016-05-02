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

from django.contrib.auth import authenticate, login, logout
#forms
from main.forms import *


# import requests
# import os
# import sys


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

# def details_view(request):
# 	xtype = request.GET.get('xtype', '')
# 	xid = request.GET.get('xid', '')
# 	context = {}
# 	model = None
# 	if xtype == "genre":
# 		model = Genre
# 		dic = {'genre_id':xid}
# 	if xtype == "album":
# 		model = Album
# 		dic = {'album_id':xid}
# 	if xtype == "artist":
# 		model = Artist
# 		dic = {'artist_id':xid}
# 	if xtype == "track":
# 		model = Track
# 		dic = {'track_id':xid}

# 	grabit(xtype , xid)
# 	try:
# 		xobject = model.objects.get(**dic)

# 	except Exception, e:
# 		xobject = "Failed"
# 	context['xtype'] = xtype
# 	context['xobject'] = xobject
# 	return render_to_response('details.html', context, context_instance=RequestContext(request))


def list_view(request):
	context = {}
	type_of_search = request.GET.get('type', None)
	search_id = request.GET.get('id', None)
	apartments = []
	if type_of_search == 'gov':
		gov = Gov.objects.get(id=search_id)

		for area in gov.area_set.all():
			for apartment in area.apartment_set.all():
				apartments.append(apartment)

		context['apartments'] = apartments

	elif type_of_search == 'area':
		area = Area.objects.get(id=search_id)
		for apartment in area.apartment_set.all():
			apartments.append(apartment)
		context['apartments'] = apartments
	return render(request, 'list_view.html', context)



def apartment_detail(request, pk):
	context = {}
	apartment = Apartment.objects.get(pk=pk)
	context['apartment'] = apartment
	return render(request, 'detail.html', context)

@staff_member_required
def create_apartment(request):
	context = {}
	form = CreateApartmentForm()
	context['form'] = form
	if request.method == 'POST':
		form = CreateApartmentForm(request.POST)

		if form.is_valid():
			form.save()

		context['form'] = form
	return render_to_response('create_apartment.html', context_instance=RequestContext(request))

@staff_member_required
def edit_apartment(request, pk):
	context = {}
	apartment = Apartment.objects.get(pk=pk)
	context['apartment'] = apartment
	form = CreateApartmentForm(request.POST or None, instance=apartment)
	context['form'] = form
	if form.is_valid():
		form.save()
		return redirect('/edit_apartment/%s/' % apartment.name)
	return render_to_response('edit_apartment.html', context_instance=RequestContext(request))

@staff_member_required
def delete_apartment(request, pk):
	apartment = Apartment.objects.get(pk=pk)
	apartment.delete()
	return redirect('/create_apartment/%s' % apartment.name)


def sign_up(request):
	context = {}
	context['form'] = CustomUserCreationForm(request.POST)
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email', None)
			password = form.cleaned_data.get('password1', None)
			auth_user = authenticate(username=email, password=password)
			try:
				login(request, auth_user)
			except Exception, e:
				print e
				return HttpResponse('Error, try again <a href="/signup/">here</a>')
	return render(request, 'signup.html', context)


def login_view(request):
	context = {}
	context['form'] = CustomUserLoginForm()
	if request.method == 'POST':
		form = CustomUserLoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email', None)
			password = form.cleaned_data.get('password', None)
			auth_user = authenticate(username=email, password=password)
			try:
				login(request, auth_user)
			except Exception, e:
				message = """
				username or password incorrect, try again!
				<a href='/login/'>login</a>
				"""
				return HttpResponse(message)
	return render(request, 'login.html', context)


def logout_view(request):
	logout(request)
	return redirect('/signup/')

def profile_page(request):
	context = {}
	print request.user
	print request.user.pk
	try:
		context['user'] = CustomUser.objects.get(pk=request.user.pk)
	except Exception, e:
		raise Http404('404')
	return render(request, 'profile_page.html', context)

def edit_profile(request):
	context = {}
	try:
		user = CustomUser.objects.get(pk=request.user.pk)
	except Exception, e:
		raise Http404('404')
	form = EditProfileForm(request.POST or None, instance=user)
	context['form'] = form
	if form.is_valid():
		form.save()
		return redirect('/profile/')
	else:
		print form.errors
	return render(request, 'edit_profile.html', context)

def homepage(request):
	return render(request, 'index.html')

def search_view(request):
    context = {}
    context['form'] = Searchbox()
    if request.method == 'POST':
        form = Searchbox(request.POST or None)
        context['form'] = form
        if form.is_valid():
            x = {}
            if form.cleaned_data.get('parking', None) != None:
                x['parking__get']=form.cleaned_data.get('parking', '0')
            if form.cleaned_data.get('internet', None) is True:
                x['internet']=form.cleaned_data.get('internet', None)
            if form.cleaned_data.get('pets', None) is True:
                x['pets']=form.cleaned_data.get('pets', None)
            if form.cleaned_data.get('maidroom', None) is True:
                x['maidroom']=form.cleaned_data.get('maidroom', None)
            if form.cleaned_data.get('lift', None) is True:
                x['lift']=form.cleaned_data.get('lift', None)
            if form.cleaned_data.get('balcony', None) is True:
                x['balcony']=form.cleaned_data.get('balcony', None)
            if form.cleaned_data.get('bills', None) is True:
                x['bills']=form.cleaned_data.get('bills', None)
            if form.cleaned_data.get('area', None) != None:
                area=form.cleaned_data.get('area', None)
                search_result = area.apartment_set.filter(**x)
                # print search_result
            else:
                areas=Area.objects.all()
                search_result = []
                for area in areas:
                    if not area.apartment_set.filter(**x):
                        empty = 'empty'
                    else:
                        search_result.append(area.apartment_set.filter(**x))
                print search_result
                context['apartments'] = search_result
            return render(request, 'list_view.html', context)
    print 'first'
    return render(request, 'search.html', context)
