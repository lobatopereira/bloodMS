import datetime
from django.db.models import Count, Q
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from bloodstock.models import BloodStock,BloodGroup
from custom.utils import getMonthName
from doador.models import DoadorBloodPackage
from enfermaria.models import BloodRequest,Enfermaria
from patient.models import Patient

class APIGBloodStockB(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		group = request.user.groups.all()[0].name
		label,obj = list(),list()
		BloodStockList = BloodStock.objects.all()
		if group == "admin" or group == "ubloodbank":
			for x in BloodStockList.iterator():
				label.append(x.bloodGroup.name)
				obj.append(x.amount_of_package)
			data = { 'label': label, 'obj': obj, }
			return Response(data)

class APIGBloodRequestEnfB(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		group = request.user.groups.all()[0].name
		label,obj = list(),list()
		enfermaria = Enfermaria.objects.all()
		if group == "admin" or group == "ubloodbank":
			for x in enfermaria:
				label.append(x.name)
				totalRequest = BloodRequest.objects.filter(enfermaria__id=x.id).count()
				obj.append(totalRequest)
			data = { 'label': label, 'obj': obj }
			return Response(data)

class APIGBloodBankedUsedOutStockThisYearB(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		group = request.user.groups.all()[0].name
		today = datetime.date.today()
		# ran tama Uza tuir fulan
		label,obj1,obj2,obj3,obj4 = list(),list(),list(),list(),list()
		for i in range(12):
			monthName = getMonthName(i+1)
			label.append(monthName)
			totalRanTama = DoadorBloodPackage.objects.filter(donationdate__month=i+1,donationdate__year=int(today.year-1)).all()
			totalPakoteTama = 0
			for x in totalRanTama:
				totalPakoteTama += x.package
			obj1.append(totalPakoteTama)

			totalRanUza = DoadorBloodPackage.objects.filter(donationdate__month=i+1,donationdate__year=int(today.year-1),packageStatus="Used").all()
			totalPakoteUza = 0
			for x in totalRanUza:
				totalPakoteUza += x.package
			obj2.append(totalPakoteUza)
			
			totalRanArmazen = DoadorBloodPackage.objects.filter(donationdate__month=i+1,donationdate__year=int(today.year-1),packageStatus="Banked").all()
			totalPakoteArmazen = 0
			for x in totalRanArmazen:
				totalPakoteArmazen += x.package
			obj3.append(totalPakoteArmazen)

			totalRanSai = BloodRequest.objects.filter(bloodrequestresponse__date_of_response__month=i+1,bloodrequestresponse__date_of_response__year=int(today.year-1),bloodrequestresponse__is_sent=True).prefetch_related('bloodrequestresponse').all()
			totalPakoteSai = 0
			for x in totalRanSai:
				totalPakoteSai += x.package
			obj4.append(totalPakoteSai)
		data = { 'label': label, 'obj1': obj1, 'obj2': obj2, 'obj3': obj3, 'obj4': obj4, 'obj1a': "Ran Tama", 'obj2a': "Ran Uza", 'obj3a': "Armazena", 'obj4a': "Sai"}
		return Response(data)
			
class APIGBloodBankedUsedOutStockByYearB(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		group = request.user.groups.all()[0].name
		today = datetime.date.today()
		# ran tama Uza tuir fulan
		label,obj1,obj2,obj3,obj4 = list(),list(),list(),list(),list()
		tinanPakoteRan = DoadorBloodPackage.objects.filter().distinct().values('donationdate__year').all().order_by('-donationdate__year')
		for tinan in tinanPakoteRan:
			totalRanTama = DoadorBloodPackage.objects.filter(donationdate__year=tinan['donationdate__year']).all()
			totalPakoteTama = 0
			for x in totalRanTama:
				totalPakoteTama += x.package
			obj1.append(totalPakoteTama)
			totalRanUza = DoadorBloodPackage.objects.filter(donationdate__year=tinan['donationdate__year'],packageStatus="Used").all()
			totalPakoteUza = 0
			for x in totalRanUza:
				totalPakoteUza += x.package
			obj2.append(totalPakoteUza)
			totalRanArmazen = DoadorBloodPackage.objects.filter(donationdate__year=tinan['donationdate__year'],packageStatus="Banked").all()
			totalPakoteArmazen = 0
			for x in totalRanArmazen:
				totalPakoteArmazen += x.package
			obj3.append(totalPakoteArmazen)
			totalRanSai = BloodRequest.objects.filter(bloodrequestresponse__date_of_response__year=tinan['donationdate__year'],bloodrequestresponse__is_sent=True).prefetch_related('bloodrequestresponse').all()
			totalPakoteSai = 0
			for x in totalRanSai:
				totalPakoteSai += x.package
			obj4.append(totalPakoteSai)
			label.append(tinan['donationdate__year'])
		data = {'label': label, 'obj1': obj1, 'obj2': obj2, 'obj3': obj3, 'obj4': obj4, 'obj1a': "Ran Tama", 'obj2a': "Ran Uza", 'obj3a': "Armazena", 'obj4a': "Sai"}
		return Response(data)
			
class APIGBloodBankedUsedStockB(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		group = request.user.groups.all()[0].name
		totalActivuPackage = DoadorBloodPackage.objects.filter(packageStatus="Banked").count()
		totalUsedPackage = DoadorBloodPackage.objects.filter(packageStatus="Used").count()
		label = ["Armazena Hela","Uza Ona"]
		obj = [totalActivuPackage,totalUsedPackage]
		data = { 'label': label, 'obj': obj }
		return Response(data)

class APIGPatientSexBloodGroup(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		group = request.user.groups.all()[0].name
		label,obj1,obj2 = list(),list(),list()
		bloodGroup = BloodGroup.objects.all().order_by('name')
		seksu = Patient.objects.filter().distinct().values('sex').order_by('sex').all()
		for x in bloodGroup:
			patientM = Patient.objects.filter(bloodGroup__id=x.id,sex='Mane').order_by('bloodGroup').count()
			patientF = Patient.objects.filter(bloodGroup__id=x.id,sex='Feto').order_by('bloodGroup').count()
			label.append(x.name)
			obj1.append(patientM)
			obj2.append(patientF)
		data = { 'label': label, 'obj1': obj1, 'obj2': obj2, 'obj1a': "Mane", 'obj2a': "Feto" }
		return Response(data)
