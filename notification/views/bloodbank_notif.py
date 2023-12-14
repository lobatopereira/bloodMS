from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from patient.forms import PatientForm
from patient.models import Patient
from bloodstock.models import BloodGroup,BloodStock
from custom.utils import *
from enfermaria.models import Enfermaria,BloodRequest
from django.contrib import messages
from users.decorators import allowed_users
from users.utils import c_user_enf

def NotifListaPediduRAN(request):
	objects = BloodRequest.objects.filter(is_sent=True, is_approved=False).order_by('-date_of_request').all()
	# table footer
	BloodStockList = BloodStock.objects.all()
	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalPasiente = BloodRequest.objects.filter(is_sent=True, is_approved=False,patient__bloodGroup__id=x.id).all().count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalPasiente':totalPasiente})
	context = {
		"title":"Lista Pedidu Pakote RAN",
		"objects":objects,
		"BloodStockList":BloodStockList,
		"listaPediduAll":objects.count(),
		"page":"list",
		"sumariuGrupuRan":sumariuGrupuRan,
	}

	return render (request, 'bloodbank/BloodPackageRequestList.html',context)

def NotifListaPediduBazeiaGrupuRAN(request,idGrupuRan):
	objects = BloodRequest.objects.filter(is_sent=True, is_approved=False,patient__bloodGroup__id=idGrupuRan).order_by('-date_of_request').all()
	listaPediduAll = BloodRequest.objects.filter(is_sent=True, is_approved=False).all()
	# table footer
	BloodStockList = BloodStock.objects.all()
	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalPasiente = BloodRequest.objects.filter(is_sent=True, is_approved=False,patient__bloodGroup__id=x.id).all().count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalPasiente':totalPasiente})
	context = {
		"title":"Lista Pedidu Pakote RAN",
		"objects":objects,
		"BloodStockList":BloodStockList,
		"listaPediduAll":listaPediduAll.count(),
		"page":"list",
		"sumariuGrupuRan":sumariuGrupuRan,
	}

	return render (request, 'bloodbank/BloodPackageRequestList.html',context)