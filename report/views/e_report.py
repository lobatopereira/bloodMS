from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from bloodstock.models import BloodStock,BloodGroup
from doador.models import DoadorBloodPackage
from patient.models import Patient
from enfermaria.models import Enfermaria,BloodRequest,BloodRequestResponse
from custom.utils import getMonthName
from users.utils import c_user_enf
import datetime
from users.decorators import allowed_users


@login_required
def EReportDashTabular(request):
	group = request.user.groups.all()[0].name
	enfermaria = c_user_enf(request.user)
	enfermariaData = get_object_or_404(Enfermaria,id=enfermaria.id)
	totalRequestPackage = BloodRequest.objects.filter(enfermaria=enfermariaData).count()
	totalPatientEnfermaria = Patient.objects.filter(enfermaria=enfermariaData).count()
	
	# SumariuPasiente
	SumariuPasiente = []
	bloodGroup = BloodGroup.objects.all().order_by('name')
	seksu = Patient.objects.filter(enfermaria=enfermariaData).distinct().values('sex').order_by('sex').all()
	for x in seksu:
		totalpatient = []
		for i in bloodGroup:
			patient = Patient.objects.filter(enfermaria=enfermariaData,bloodGroup__id=i.id,sex=x['sex']).order_by('bloodGroup').count()
			totalpatient.append({"name":i.name,"total":patient})
		SumariuPasiente.append([x,totalpatient])

	context ={
		"title":f"Pajina Relatoriu ho formatu Tabular",
		"report_active":"active","SumariuPasiente":SumariuPasiente,"bloodGroup":bloodGroup,
		"totalRequestPackage":totalRequestPackage,"totalPatientEnfermaria":totalPatientEnfermaria,
	}
	return render(request, "e_report/dash_tabular.html",context)