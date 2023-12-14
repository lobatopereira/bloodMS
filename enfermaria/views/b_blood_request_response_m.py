from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ..forms import BloodRequestForm,BloodRequestForm1,BloodRequestResponseForm
from patient.forms import PatientForm
from patient.models import Patient
from bloodstock.models import BloodStock,BloodGroup
from custom.utils import *
from enfermaria.models import Enfermaria,BloodRequest,BloodRequestResponse
from doador.models import Doador,DoadorBloodPackage
from django.contrib import messages
from users.decorators import allowed_users

@login_required
def BBloodRequestResponseAdd(request,bloodRequestID):
	group = request.user.groups.all()[0].name
	bloodRequest = get_object_or_404(BloodRequest,hashed=bloodRequestID)
	bloodRequest.is_respond = True
	bloodGroup = bloodRequest.patient.bloodGroup.name
	listaDoador = DoadorBloodPackage.objects.filter(bloodGroup__name=bloodGroup,packageStatus="Banked").order_by('id')
	enfermariaData = get_object_or_404(Enfermaria,id=bloodRequest.enfermaria.id)
	if request.method == 'POST':
		doador = request.POST.getlist('doador')
		if doador != []:
			for x in doador:
				doadorBloodPackage = get_object_or_404(DoadorBloodPackage,id=x)
				doadorBloodPackage.packageStatus = "Used"
				_, newid = getlastid(BloodRequestResponse)
				hashid = hash_md5(str(newid))
				form = BloodRequestResponseForm(request.POST)
				if form.is_valid():
					instance = form.save(commit=False)
					instance.bloodRequest = bloodRequest
					instance.doador = doadorBloodPackage
					instance.hashed = hashid
					instance.user_created = request.user
					bloodstock = BloodStock.objects.filter(bloodGroup__name=bloodGroup).last()
					if bloodstock:
						new_amount_of_package = int(bloodstock.amount_of_package)-int(doadorBloodPackage.package)
						BloodStock.objects.filter(bloodGroup__name=bloodGroup).update(amount_of_package=new_amount_of_package)
					bloodRequest.save()
					doadorBloodPackage.save()
					instance.save()
			messages.success(request, f'Dadus Pedidu ba RAN responde ona ho susesu.')
			return redirect('e-blood-request-response-detail',bloodRequest.hashed)
		else:
			messages.error(request, f'Dadus Pakote RAN atu responde seidauk iha.')
			return redirect('b-blood-request-response-add',bloodRequestID)

	else:
		form = BloodRequestResponseForm()

	context ={
		"title":f"Responde Dadus Pedidu ba RAN husi enfermaria {enfermariaData.name}",
		"page":"form",
		"form":form,
		"listaDoador":listaDoador,
	}
	return render(request, "BloodRequest/BloodRequestResponseList.html",context)

@login_required
def BBloodRequestResponseDetail(request,bloodRequestID):
	group = request.user.groups.all()[0].name
	bloodRequest = get_object_or_404(BloodRequest,hashed=bloodRequestID)
	bloodRequestResponse = BloodRequestResponse.objects.filter(bloodRequest=bloodRequest)
	context ={
		"title":f"Detallu Responde Dadus Pedidu ba RAN husi enfermaria {bloodRequest.enfermaria.name}",
		"page":"detail",
		"bloodRequest":bloodRequest,
		"bloodRequestResponse":bloodRequestResponse,
	}
	return render(request, "BloodRequest/BloodRequestResponseList.html",context)

@login_required
def BBloodRequestResponseDelete(request,bloodRequestID):
	group = request.user.groups.all()[0].name
	bloodRequest = get_object_or_404(BloodRequest,hashed=bloodRequestID)
	bloodRequest.is_respond = False
	bloodRequest.save()
	bloodGroup = bloodRequest.patient.bloodGroup.name
	bloodRequestResponse = BloodRequestResponse.objects.filter(bloodRequest=bloodRequest)
	for x in bloodRequestResponse:
		doadorBloodPackage = get_object_or_404(DoadorBloodPackage,id=x.doador.id)
		doadorBloodPackage.packageStatus = "Banked"
		doadorBloodPackage.save()
		bloodRequestResponse.delete()
		bloodstock = BloodStock.objects.filter(bloodGroup__name=bloodGroup).last()
		if bloodstock:
			new_amount_of_package = int(bloodstock.amount_of_package)+int(doadorBloodPackage.package)
			BloodStock.objects.filter(bloodGroup__name=bloodGroup).update(amount_of_package=new_amount_of_package)
	messages.success(request, f'Dadus Resposta ba Pedidu ba RAN Hamoos ho susesu.')
	return redirect('NotifListaPediduRAN')

@login_required
def BBloodRequestResponseKonfirma(request,bloodRequestID):
	group = request.user.groups.all()[0].name
	bloodRequest = get_object_or_404(BloodRequest,hashed=bloodRequestID)
	bloodRequest.is_approved = True
	bloodRequest.save()
	bloodGroup = bloodRequest.patient.bloodGroup.name
	bloodRequestResponse = BloodRequestResponse.objects.filter(bloodRequest=bloodRequest)
	for x in bloodRequestResponse:
		bloodRequestResponse.update(is_locked = True,is_sent=True)
	messages.success(request, f'Dadus Resposta ba Pedidu ba RAN Konfirmadu ho susesu.')
	return redirect('e-blood-request-response-detail',bloodRequest.hashed)

@login_required
def ListBloodRequestRespondTrue(request):
	objects = BloodRequest.objects.filter(is_sent=True, is_approved=True).all()
	# table footer
	BloodStockList = BloodStock.objects.all()
	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalPasiente = BloodRequest.objects.filter(is_sent=True, is_approved=True,patient__bloodGroup__id=x.id).all().count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalPasiente':totalPasiente})
	context = {
		"title":"Lista Pedidu Pakote RAN ne'ebe hetan Resposta ona",
		"objects":objects,
		"BloodStockList":BloodStockList,
		"listaPediduAll":objects.count(),
		"page":"list",
		"sumariuGrupuRan":sumariuGrupuRan,
	}

	return render (request, 'BloodResponse/BloodPackageRequestApprovedList.html',context)

@login_required
def ListBloodGroupRequestRespondTrue(request,idGrupuRan):
	grupuRan = BloodGroup.objects.get(id=idGrupuRan)
	objects = BloodRequest.objects.filter(is_sent=True, is_approved=True,patient__bloodGroup__id=idGrupuRan).all()
	listaPediduAll = BloodRequest.objects.filter(is_sent=True, is_approved=True).all()
	# table footer
	BloodStockList = BloodStock.objects.all()
	listaGrupuRan = BloodGroup.objects.all()
	sumariuGrupuRan = []
	for x in listaGrupuRan.iterator():
		totalPasiente = BloodRequest.objects.filter(is_sent=True, is_approved=True,patient__bloodGroup__id=x.id).all().count()
		sumariuGrupuRan.append({'id':x.id,'grupuran':x.name,'totalPasiente':totalPasiente})
	context = {
		"title":f"Lista Pedidu Pakote Grupu RAN {grupuRan.name} ne'ebe hetan Resposta ona",
		"objects":objects,
		"BloodStockList":BloodStockList,
		"listaPediduAll":listaPediduAll.count(),
		"page":"list",
		"sumariuGrupuRan":sumariuGrupuRan,
	}

	return render (request, 'BloodResponse/BloodPackageRequestApprovedList.html',context)

