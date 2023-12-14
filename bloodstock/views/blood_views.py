from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ..forms import *
from custom.utils import *
from bloodstock.models import BloodGroup,BloodStock
from django.contrib import messages
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin'])
def BloodGroupList(request):
	BloodGroupList = BloodGroup.objects.all()
	context = {
		"title":"Lista Grupu Ran",
		"page":"list",
		"BloodGroupList":BloodGroupList,
	}
	return render(request, "grupuran/BloodGroupList.html",context)

@login_required
@allowed_users(allowed_roles=['admin'])
def addGrupuRan(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		_, newid = getlastid(BloodGroup)
		form = BloodGroupForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			naran = instance.name
			instance.save()
			BloodStock.objects.create(bloodGroup=instance,amount_of_package=0)
			messages.info(request, f'Dadus Grupu Ran {naran} rejista ho susesu.')
			return redirect('BloodGroupList')
	else:
		form = BloodGroupForm()

	context ={
		"title":"Rejista dadus Grupu Ran",
		"page":"form",
		"form":form,
	}
	return render(request, "grupuran/BloodGroupList.html",context)

@login_required
@allowed_users(allowed_roles=['admin'])
def updateGrupuRan(request,id):
	group = request.user.groups.all()[0].name
	bloodgroupData = get_object_or_404(BloodGroup,id=id)
	if request.method == 'POST':
		form = BloodGroupForm(request.POST,instance=bloodgroupData)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.info(request, f'Dadus Grupu Ran altera ho susesu.')
			return redirect('BloodGroupList')
	else:
		form = BloodGroupForm(instance=bloodgroupData)

	context ={
		"title":"Altera dadus Grupu Ran",
		"page":"form",
		"form":form,
	}
	return render(request, "enfermaria/EnfermariaList.html",context)

@login_required
@allowed_users(allowed_roles=['admin'])
def deleteGrupuRan(request,id):
	group = request.user.groups.all()[0].name
	bloodgroupData = get_object_or_404(BloodGroup,id=id)
	naran = bloodgroupData.name
	bloodgroupData.delete()
	messages.error(request, f'Dadus Grupu Ran {bloodgroupData} hamoos ho susesu.')
	return redirect('BloodGroupList')