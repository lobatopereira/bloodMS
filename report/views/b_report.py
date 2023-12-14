from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from bloodstock.models import BloodStock,BloodGroup
from doador.models import DoadorBloodPackage
from patient.models import Patient
from enfermaria.models import BloodRequest,BloodRequestResponse,Enfermaria
from custom.utils import getMonthName
from users.decorators import allowed_users
import datetime

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def BReportDashTabular(request):
	group = request.user.groups.all()[0].name
	
	totalActivuPackage = DoadorBloodPackage.objects.filter(packageStatus="Banked").count()
	totalUsedPackage = DoadorBloodPackage.objects.filter(packageStatus="Used").count()
	bloodStockList = BloodStock.objects.all()
	stockSumary = []
	totalstock = 0
	for stock in bloodStockList:
		totalstock += stock.amount_of_package
		stockSumary.append([stock.bloodGroup,stock.amount_of_package])
	stockSumary.append(["Total",totalstock])

	today = datetime.date.today()
	# ran tama Uza tuir fulan
	dadus_tinan_agora = []
	totalPakoteTamaA = 0
	totalPakoteUzaA = 0
	totalPakoteArmazenA = 0
	totalPakoteSaiA = 0
	for i in range(12):
		monthName = getMonthName(i+1)
		totalRanTama = DoadorBloodPackage.objects.filter(donationdate__month=i+1,donationdate__year=today.year).all()
		totalPakoteTama = 0
		for x in totalRanTama:
			totalPakoteTama += x.package
			totalPakoteTamaA += x.package
		totalRanUza = DoadorBloodPackage.objects.filter(donationdate__month=i+1,donationdate__year=today.year,packageStatus="Used").all()
		totalPakoteUza = 0
		for x in totalRanUza:
			totalPakoteUza += x.package
			totalPakoteUzaA += x.package
		totalRanArmazen = DoadorBloodPackage.objects.filter(donationdate__month=i+1,donationdate__year=today.year,packageStatus="Banked").all()
		totalPakoteArmazen = 0
		for x in totalRanArmazen:
			totalPakoteArmazen += x.package
			totalPakoteArmazenA += x.package
		totalRanSai = BloodRequest.objects.filter(bloodrequestresponse__date_of_response__month=i+1,bloodrequestresponse__date_of_response__year=today.year,bloodrequestresponse__is_sent=True).prefetch_related('bloodrequestresponse').all()
		totalPakoteSai = 0
		for x in totalRanSai:
			totalPakoteSai += x.package
			totalPakoteSaiA += x.package
		dadus_tinan_agora.append([i+1,monthName,totalPakoteTama,totalPakoteUza,totalPakoteArmazen,totalPakoteSai])
	dadus_tinan_agora.append(["","Total",totalPakoteTamaA,totalPakoteUzaA,totalPakoteArmazenA,totalPakoteSaiA])
	# SumariuPasiente
	SumariuPasiente = []
	bloodGroup = BloodGroup.objects.all().order_by('name')
	seksu = Patient.objects.filter().distinct().values('sex').order_by('sex').all()
	for x in seksu:
		totalpatient = []
		for i in bloodGroup:
			patient = Patient.objects.filter(bloodGroup__id=i.id,sex=x['sex']).order_by('bloodGroup').count()
			totalpatient.append({"name":i.name,"total":patient})
		SumariuPasiente.append([x,totalpatient])
	
	# SumariuPasiente1 = []
	# for x in SumariuPasiente:
	# 	print("SumariuPasiente:",x)
	# 	print("SumariuPasiente:",x[0]['sex'],x[1][0]['name'],x[1][0]['total'])
	# 	SumariuPasiente1.append({x[0]['sex']})
	# # SumariuPasiente1.append(["total",totalpatient])

	# Sumariu tuir tinan
	dadus_pakote_tuir_tinan = []
	totalPakoteTamaA = 0
	totalPakoteUzaA = 0
	totalPakoteArmazenA = 0
	totalPakoteSaiA = 0
	tinanPakoteRan = DoadorBloodPackage.objects.filter().distinct().values('donationdate__year').all().order_by('-donationdate__year')
	for tinan in tinanPakoteRan:
		totalRanTama = DoadorBloodPackage.objects.filter(donationdate__year=tinan['donationdate__year']).all()
		totalPakoteTama = 0
		for x in totalRanTama:
			totalPakoteTama += x.package
			totalPakoteTamaA += x.package
		totalRanUza = DoadorBloodPackage.objects.filter(donationdate__year=tinan['donationdate__year'],packageStatus="Used").all()
		totalPakoteUza = 0
		for x in totalRanUza:
			totalPakoteUza += x.package
			totalPakoteUzaA += x.package
		totalRanArmazen = DoadorBloodPackage.objects.filter(donationdate__year=tinan['donationdate__year'],packageStatus="Banked").all()
		totalPakoteArmazen = 0
		for x in totalRanArmazen:
			totalPakoteArmazen += x.package
			totalPakoteArmazenA += x.package
		totalRanSai = BloodRequest.objects.filter(bloodrequestresponse__date_of_response__year=tinan['donationdate__year'],bloodrequestresponse__is_sent=True).prefetch_related('bloodrequestresponse').all()
		totalPakoteSai = 0
		for x in totalRanSai:
			totalPakoteSai += x.package
			totalPakoteSaiA += x.package
		dadus_pakote_tuir_tinan.append([tinan['donationdate__year'],totalPakoteTama,totalPakoteUza,totalPakoteArmazen,totalPakoteSai])
	dadus_pakote_tuir_tinan.append(["Total",totalPakoteTamaA,totalPakoteUzaA,totalPakoteArmazenA,totalPakoteSaiA])

	# Sumariu pedidu
	SumariuPedidu = list()
	enfermaria = Enfermaria.objects.all()
	for enf in enfermaria:
		totalRequest = BloodRequest.objects.filter(enfermaria__id=enf.id).count()
		SumariuPedidu.append([enf.id,enf.name,totalRequest])



	context ={
		"title":f"Pajina Relatoriu ho formatu Tabular","bloodGroup":bloodGroup,"dadus_pakote_tuir_tinan":dadus_pakote_tuir_tinan,
		"report_active":"active","currentYear":today.year,"dadus_tinan_agora":dadus_tinan_agora,"SumariuPasiente":SumariuPasiente,
		"totalActivuPackage":totalActivuPackage,"totalUsedPackage":totalUsedPackage,"stockSumary":stockSumary,"SumariuPedidu":SumariuPedidu,
	}
	return render(request, "b_report/dash_tabular.html",context)