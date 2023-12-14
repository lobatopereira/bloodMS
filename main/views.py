from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from custom.utils import *
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from bloodstock.models import BloodGroup,BloodStock

# from ipware import get_client_ip
# from ip2geotools.databases.noncommercial import DbIpCity

# Create your views here.

@login_required
def home(request):
	# ip, is_routable = get_client_ip(request)
	# print("IP:",ip)
	# try:
	# 	response = DbIpCity.get(ip, api_key='free')
	# 	country = response.country + " | "+ response.city
	# except :
	# 	country = "koko"
	# print("country:",response)
	bloodStock = BloodStock.objects.all()
	context = {
		"title":"Sistema Informasaun Stock Ran",
		"bloodStock":bloodStock,
	}

	return render (request, 'index/indexAdmin.html',context)