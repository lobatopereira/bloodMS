from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ..forms import *
from custom.utils import *
from bloodstock.models import BloodGroup
from enfermaria.models import Enfermaria,BloodRequest
from django.contrib import messages
from users.decorators import allowed_users
from users.utils import c_user_enf

@login_required
def EBloodRequestList(request):
	enfermaria = c_user_enf(request.user)
	enfermariaData = get_object_or_404(Enfermaria,id=enfermaria.id)
	BloodRequestList = BloodRequest.objects.filter(enfermaria=enfermariaData).all()

	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalBloodRequest = BloodRequest.objects.filter(patient__bloodGroup__id=x.id,enfermaria=enfermariaData).count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalBloodRequest':totalBloodRequest})
	context = {
		"title":"Lista Pedidu Pakote RAN",
		"page":"list",
		"BloodRequestList":BloodRequestList,
		"listaPediduAll":BloodRequestList.count(),
		"sumariuGrupuRan":sumariuGrupuRan,
		"active_request":"active",
	}
	return render(request, "BloodRequest/BloodRequestList.html",context)

@login_required
def EBloodGroupRequestList(request,idGrupuRan):
	enfermaria = c_user_enf(request.user)
	enfermariaData = get_object_or_404(Enfermaria,id=enfermaria.id)
	bloodGroupData = get_object_or_404(BloodGroup,id=idGrupuRan)
	BloodRequestList = BloodRequest.objects.filter(enfermaria=enfermariaData,patient__bloodGroup=bloodGroupData).all()

	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalBloodRequest = BloodRequest.objects.filter(patient__bloodGroup__id=x.id).count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalBloodRequest':totalBloodRequest})
	context = {
		"title":"Lista Pedidu Pakote RAN",
		"page":"list",
		"BloodRequestList":BloodRequestList,
		"listaPediduAll":BloodRequestList.count(),
		"sumariuGrupuRan":sumariuGrupuRan,
		"active_request":"active",
	}
	return render(request, "BloodRequest/BloodRequestList.html",context)