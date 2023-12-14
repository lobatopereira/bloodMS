from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ..forms import *
from custom.utils import *
from enfermaria.models import Enfermaria
from django.contrib import messages
from users.decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin'])
def EnfermariaList(request):
	EnfermariaList = Enfermaria.objects.all()
	context = {
		"title":"Lista Enfermaria",
		"page":"list",
		"EnfermariaList":EnfermariaList,
	}
	return render(request, "enfermaria/EnfermariaList.html",context)

@login_required
@allowed_users(allowed_roles=['admin'])
def addEnfermaria(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		_, newid = getlastid(Enfermaria)
		form = EnfermariaForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			naran = instance.name
			instance.save()
			messages.info(request, f'Dadus Enfermaria {naran} rejista ho susesu.')
			return redirect('EnfermariaList')
	else:
		form = EnfermariaForm()

	context ={
		"title":"Rejista dadus Enfermaria",
		"page":"form",
		"form":form,
	}
	return render(request, "enfermaria/EnfermariaList.html",context)

@login_required
@allowed_users(allowed_roles=['admin'])
def updateEnfermaria(request,id):
	group = request.user.groups.all()[0].name
	enfermariaData = get_object_or_404(Enfermaria,id=id)
	if request.method == 'POST':
		form = EnfermariaForm(request.POST,instance=enfermariaData)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.info(request, f'Dadus Enfermaria altera ho susesu.')
			return redirect('EnfermariaList')
	else:
		form = EnfermariaForm(instance=enfermariaData)

	context ={
		"title":"Altera dadus Enfermaria",
		"page":"form",
		"form":form,
	}
	return render(request, "enfermaria/EnfermariaList.html",context)

@login_required
@allowed_users(allowed_roles=['admin'])
def deleteEnfermaria(request,id):
	enfermariaData = get_object_or_404(Enfermaria,id=id)
	naran = enfermariaData.name
	enfermariaData.delete()
	messages.error(request, f'Dadus Enfermaria {naran} hamoos ho susesu.')
	return redirect('EnfermariaList')

