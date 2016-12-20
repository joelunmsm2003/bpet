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
from app.settings import *
import datetime



@csrf_exempt
def registra(request):

    if request.method == 'POST':

    	data = json.loads(request.body)

		for d in data:

			if d == 'name':

				name = data['name']

			if d == 'email':

				email = data['email']


			if d == 'direccion':

				direccion = data['direccion']


			if d == 'nombre_mascota':

				nombre_mascota = data['nombre_mascota']

			if d == 'raza':

				raza = data['raza']

			if d == 'horario':

				horario = data['horario']






        data_json = simplejson.dumps('icon')

        return HttpResponse(data_json, content_type="application/json")
