from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from bloodstock.models import BloodStock
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def BDashCharts(request):
	group = request.user.groups.all()[0].name
	context ={
		"title":f"Pajina Relatoriu ho formatu Grafiku",
		"report_active":"active",
	}
	return render(request, "b_charts/dash.html",context)

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def ChartStockRan(request):
	group = request.user.groups.all()[0].name
	labels = []
	data = []
	BloodStockList = BloodStock.objects.all()
	if group == "admin" or group == "ubloodbank" or group == "uenfermaria":
		for x in BloodStockList.iterator():
			labels.append(x.bloodGroup.name)
			data.append(x.amount_of_package)
	return JsonResponse(data={
		'labels':labels,
		'data':data,
		})