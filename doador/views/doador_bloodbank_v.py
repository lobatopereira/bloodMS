from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ..models import Doador,DoadorBloodPackage
from custom.utils import *
from bloodstock.models import BloodGroup
from patient.models import Patient
from django.contrib import messages
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def DoadorList(request):
	doadorList = Doador.objects.all()
	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalDoador = Doador.objects.filter(bloodGroup__id=x.id).count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalDoador':totalDoador})
	context = {
		"title":"Lista Doador",
		"page":"list",
		"sumariuGrupuRan":sumariuGrupuRan,
		"doadorList":doadorList,
		"listaDoadorCount":doadorList.count(),
		"active_doador":"active",
	}
	return render(request, "doador_bloodbank/list.html",context)

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def DoadorListBloodGroup(request,hashid):
	grupuRanData = BloodGroup.objects.get(id=hashid)
	doadorList = Doador.objects.filter(bloodGroup=grupuRanData).all()
	listaGrupuRan = BloodGroup.objects.all()
	allDoadorList = Doador.objects.all().count()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalDoador = Doador.objects.filter(bloodGroup__id=x.id).count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalDoador':totalDoador})
	context = {
		"title":f"Lista Doador ho Grupu Ran {grupuRanData.name}",
		"page":"list",
		"sumariuGrupuRan":sumariuGrupuRan,
		"doadorList":doadorList,
		"listaDoadorCount":allDoadorList,
		"active_doador":"active",
	}
	return render(request, "doador_bloodbank/list.html",context)

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def detailDoasaunDoador(request,hashid):
	doadorData = get_object_or_404(Doador,hashed=hashid)
	listaDoasaun = DoadorBloodPackage.objects.filter(doador=doadorData)
	context = {
		"title":"Detallu Dadus Doasaun",
		"page":"detail",
		"listaDoasaun":listaDoasaun,
		"doadorData":doadorData,
		"active_doador":"active",
	}
	return render(request, "doador_bloodbank/list.html",context)