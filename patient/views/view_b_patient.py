from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ..forms import *
from custom.utils import *
from enfermaria.models import Enfermaria,BloodRequest
from bloodstock.models import BloodGroup
from patient.models import Patient
from django.contrib import messages
from users.decorators import allowed_users

def BPatientList(request):
	patientList = Patient.objects.all()
	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalPasiente = Patient.objects.filter(bloodGroup__id=x.id).count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalPasiente':totalPasiente})
	context = {
		"title":"Lista Pasiente",
		"page":"list",
		"patientList":patientList,
		"sumariuGrupuRan":sumariuGrupuRan,
		"listaPasienteCount":patientList.count(),
		"active_patient":"active",
	}
	return render(request, "bloodbank/list.html",context)

def BPatientListBloodGroup(request,hashid):
	grupuRanData = BloodGroup.objects.get(id=hashid)
	patientList = Patient.objects.filter(bloodGroup=grupuRanData)
	allPatientList = Patient.objects.all()
	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalPasiente = Patient.objects.filter(bloodGroup__id=x.id).count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalPasiente':totalPasiente})
	context = {
		"title":f"Lista Pasiente Grupu Ran {grupuRanData.name}",
		"page":"list",
		"patientList":patientList,
		"listaPasienteCount":allPatientList.count(),
		"sumariuGrupuRan":sumariuGrupuRan,
		"active_patient":"active",
	}
	return render(request, "bloodbank/list.html",context)

