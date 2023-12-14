from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ..forms import BloodRequestForm,BloodRequestForm1,BloodRequestResponseForm
from patient.forms import PatientForm
from patient.models import Patient
from bloodstock.models import BloodStock
from custom.utils import *
from enfermaria.models import Enfermaria,BloodRequest,BloodRequestResponse
from doador.models import Doador,DoadorBloodPackage
from django.contrib import messages
from users.decorators import allowed_users
from users.utils import c_user_enf

@login_required
def EBloodRequestAdd(request):
	group = request.user.groups.all()[0].name
	enfermaria = c_user_enf(request.user)
	enfermariaData = get_object_or_404(Enfermaria,id=enfermaria.id)
	if request.method == 'POST':
		requestType = request.POST.get('requestType')
		print("requestType:",requestType)
		if requestType == "ppf":
			_, newid = getlastid(BloodRequest)
			_1, newid1 = getlastid(Patient)
			hashid = hash_md5(str(newid))
			hashid1 = hash_md5(str(newid1))
			form = BloodRequestForm(request.POST)
			formPatient = PatientForm(request.POST)
			if form.is_valid() and formPatient.is_valid():
				instance = form.save(commit=False)
				instance1 = formPatient.save(commit=False)
				instance1.hashed = hashid1
				instance1.enfermaria = enfermariaData
				instance1.user_created = request.user
				instance1.save()
				instance.patient = instance1
				instance.enfermaria = enfermariaData
				instance.hashed = hashid
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Dadus Pedidu ba RAN rejista ho susesu.')
				return redirect('e-blood-request-list')
		else:
			_, newid = getlastid(BloodRequest)
			hashid = hash_md5(str(newid))
			form = BloodRequestForm1(request.POST)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.enfermaria = enfermariaData
				instance.hashed = hashid
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Dadus Pedidu ba RAN rejista ho susesu.')
				return redirect('e-blood-request-list')
	else:
		form = BloodRequestForm()
		form1 = BloodRequestForm1()
		formPatient = PatientForm()

	context ={
		"title":"Adisiona Dadus Pedidu ba RAN",
		"page":"form",
		"form":form,
		"form1":form1,
		"formPatient":formPatient,
		"active_request":"active",
	}
	return render(request, "BloodRequest/BloodRequestList.html",context)

@login_required
def LockBloodRequest(request,hashid):
	bloodRequest = get_object_or_404(BloodRequest,hashed=hashid)
	bloodRequest.is_locked = True
	bloodRequest.save()
	messages.success(request, f'Dadus Pedidu ba RAN Xave ho susesu.')
	return redirect('e-blood-request-list')

@login_required
def UnLockBloodRequest(request,hashid):
	bloodRequest = get_object_or_404(BloodRequest,hashed=hashid)
	bloodRequest.is_locked = False
	bloodRequest.save()
	messages.success(request, f'Dadus Pedidu ba RAN Loke fali ona ho susesu.')
	return redirect('e-blood-request-list')

@login_required
def SendBloodRequest(request,hashid):
	bloodRequest = get_object_or_404(BloodRequest,hashed=hashid)
	bloodRequest.is_sent = True
	bloodRequest.is_rejected = False
	bloodRequest.save()
	messages.warning(request, f'Dadus Pedidu ba RAN husi pasiente {bloodRequest.patient} iha data {bloodRequest.date_of_request} Manda ho Susesu.')
	return redirect('e-blood-request-list')


@login_required
def EBloodRequestResponseDetail(request,bloodRequestID):
	group = request.user.groups.all()[0].name
	bloodRequest = get_object_or_404(BloodRequest,hashed=bloodRequestID)
	bloodRequestResponse = BloodRequestResponse.objects.filter(bloodRequest=bloodRequest)
	context ={
		"title":f"Detallu Responde Dadus Pedidu ba RAN husi pasisente {bloodRequest.patient}",
		"page":"detail",
		"bloodRequest":bloodRequest,
		"bloodRequestResponse":bloodRequestResponse,
	}
	return render(request, "BloodRequest/EBloodRequestResponseList.html",context)

@login_required
def EBloodRequestResponseUse(request,bloodRequestResponseID):
	bloodRequestResponse = BloodRequestResponse.objects.get(id=bloodRequestResponseID)
	bloodRequestResponse.is_used = True
	bloodRequestResponse.save()
	messages.success(request, f'Dadus Pakote RAN ba pasiente {bloodRequestResponse.bloodRequest.patient} Uza ona ho Susesu.')
	return redirect('e-blood-request-response-detail',bloodRequestResponse.bloodRequest.hashed)

@login_required
def EBloodRequestResponseUnUse(request,bloodRequestResponseID):
	bloodRequestResponse = BloodRequestResponse.objects.get(id=bloodRequestResponseID)
	bloodRequestResponse.is_used = False
	bloodRequestResponse.save()
	messages.success(request, f'Dadus Pakote RAN ba pasiente {bloodRequestResponse.bloodRequest.patient} Konfigura ba seidauk uza ona ho Susesu.')
	return redirect('e-blood-request-response-detail',bloodRequestResponse.bloodRequest.hashed)

