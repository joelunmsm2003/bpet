from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin
from django.template import RequestContext
import simplejson
from django.views.decorators.csrf import csrf_exempt
import xlrd
from app.models import *


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

import time
import os
from datetime import datetime,timedelta,date
import os.path
import requests
from pets.settings import *
import datetime



@csrf_exempt
def registra(request):

	data_json = simplejson.dumps('icon')

	if request.method == 'POST':

		data = json.loads(request.body)['data']

		print data

		for d in data:

			if d == 'nombre':

				username = data['nombre']

			if d == 'password':

				password = data['password']



			if d == 'nombre_mascota':

				nombre_mascota = data['nombre_mascota']

			if d == 'raza':

				raza = data['raza']

		
		user = User.objects.create_user(username=username,password=password)

		user.save()


		Mascota(raza=raza,nombre=nombre_mascota).save()


		return HttpResponse(data_json, content_type="application/json")

	return HttpResponse(data_json, content_type="application/json")



def ValuesQuerySetToDict(vqs):

    return [item for item in vqs]



@csrf_exempt
def cuidador(request):

	data_json = simplejson.dumps('icon')

	if request.method == 'GET':

		u = AuthUser.objects.filter(tipo=1).values('id','username','direccion','distrito','porque','photo')

		u = ValuesQuerySetToDict(u)

		data_json = simplejson.dumps(u)

		return HttpResponse(data_json, content_type="application/json")


	if request.method == 'POST':

		data = json.loads(request.body)['data']

		print data

		#{u'porque': u'43', u'password': u'434', u'name': u'434', u'direccion': u'43'}


		for d in data:

			if d == 'name':

				username = data['name']

			if d == 'password':

				password = data['password']

			if d == 'direccion':

				direccion = data['direccion']

			if d == 'item':

				distrito = data['item']['id']

			if d == 'porque':

				porque = data['porque']

			if d == 'photo':

				photo = data['photo']


		user = User.objects.create_user(username=username,password=password)

		user.save()

		id_cuidador = AuthUser.objects.all().values('id').order_by('-id')[0]['id']

		u = AuthUser.objects.get(id=id_cuidador)
		u.direccion = direccion
		u.distrito= distrito
		u.porque = porque
		u.photo = photo
		u.tipo = 1
		u.save()


		return HttpResponse(data_json, content_type="application/json")

	return HttpResponse(data_json, content_type="application/json")
