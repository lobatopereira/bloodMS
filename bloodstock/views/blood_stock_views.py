from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from custom.utils import *
from bloodstock.models import BloodGroup,BloodStock
from django.contrib import messages
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def BloodStockList(request):
	BloodStockList = BloodStock.objects.all()
	context = {
		"title":"Lista Total Pakote Grupu Ran",
		"page":"BloodStockList",
		"bloodstock_active":"active",
		"BloodStockList":BloodStockList,
	}
	return render(request, "grupuran/BloodGroupList.html",context)