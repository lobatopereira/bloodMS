from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ..forms import DoadorBloodPackageForm,DoadorForm
from custom.utils import hash_md5,getlastid
from bloodstock.models import BloodGroup,BloodStock
from ..models import Doador,DoadorBloodPackage
from django.contrib import messages
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def rejistaDoador(request):
	group = request.user.groups.all()[0].name
	if request.method == "POST":
		_, newid = getlastid(Doador)
		hashid = hash_md5(str(newid))
		form = DoadorForm(request.POST,request.FILES)
		if form.is_valid() :
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = hashid
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Dadus Doador {instance.firstname} {instance.lastname} rejista ho Susesu.')
			return redirect('doasaun-add',hashid)
	else:	
		form = DoadorForm()
	context ={
		"group":group,
		"title":"Rejista Dadus Doador",
		"form":form,
		"page":"form",
		"active_doador":"active",
	}
	return render(request, "doador_bloodbank/formDoasaun.html",context)

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def updateDoador(request,hashid):
	group = request.user.groups.all()[0].name
	doadorData = get_object_or_404(Doador,hashed=hashid)
	if request.method == "POST":
		form = DoadorForm(request.POST,request.FILES,instance=doadorData)
		if form.is_valid() :
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dadus Doador {instance.firstname} {instance.lastname} altera ho Susesu.')
			return redirect('doador-list')
	else:	
		form = DoadorForm(instance=doadorData)
	context ={
		"group":group,
		"title":"Altera Dadus Doador",
		"form":form,
		"page":"form",
		"active_doador":"active",
	}
	return render(request, "doador_bloodbank/formDoasaun.html",context)

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def deleteDoador(request,hashid):
	doadorData = get_object_or_404(Doador,hashed=hashid)
	name = doadorData.firstname + " "+doadorData.lastname
	doadorData.delete()
	messages.error(request, f'Dadus Doador {name} hamoos ho Susesu.')
	return redirect('doador-list')

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def rejistaDoasaun(request,hashid):
	group = request.user.groups.all()[0].name
	doadorData = get_object_or_404(Doador,hashed=hashid)
	if request.method == "POST":
		_, newid = getlastid(DoadorBloodPackage)
		hashid = hash_md5(str(newid))
		form = DoadorBloodPackageForm(request.POST,request.FILES)
		if form.is_valid() :
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = hashid
			bloodGroup = instance.bloodGroup
			package = instance.package
			instance.user_created = request.user
			instance.doador = doadorData
			bloodstock = BloodStock.objects.filter(bloodGroup=bloodGroup).last()
			if bloodstock:
				new_amount_of_package = bloodstock.amount_of_package+package
				bloodstock.amount_of_package=new_amount_of_package
				bloodstock.save()
			else:
				bloodstock = BloodStock.objects.create(bloodGroup=bloodGroup,amount_of_package=package)

			instance.save()
			messages.success(request, f'Dadus Doasaun husi doador {doadorData.firstname} {doadorData.lastname} rejista ho Susesu.')
			return redirect('doador-detail-doasaun',doadorData.hashed)
	else:	
		form = DoadorBloodPackageForm()
	context ={
		"group":group,
		"title":f"Rejista Dadus Doasaun husi doador {doadorData.firstname} {doadorData.lastname}",
		"form":form,
		"page":"form",
		"active_doador":"active",
	}
	return render(request, "doador_bloodbank/formDoasaun.html",context)

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def updateDoasaun(request,hashid):
	group = request.user.groups.all()[0].name
	doasaunData = get_object_or_404(DoadorBloodPackage,hashed=hashid)
	orijinalBLood = doasaunData.bloodGroup
	orijinalPackage = doasaunData.package
	print("doasaunData.bloodGroup:",doasaunData.bloodGroup)
	if request.method == "POST":
		form = DoadorBloodPackageForm(request.POST,request.FILES,instance=doasaunData)
		if form.is_valid() :
			instance = form.save(commit=False)
			returnbloodstock = BloodStock.objects.filter(bloodGroup=orijinalBLood).last()
			print("returnbloodstock.bloodGroup:",returnbloodstock.bloodGroup)
			if returnbloodstock:
				print("returnbloodstock.amount_of_package:",returnbloodstock.amount_of_package)
				print("doasaunData.package:",orijinalPackage)
				new_amount_of_package = int(returnbloodstock.amount_of_package)-int(orijinalPackage)
				print("new_amount_of_package:",new_amount_of_package)
				# returnbloodstock.amount_of_package = new_amount_of_package
				BloodStock.objects.filter(bloodGroup=orijinalBLood).update(amount_of_package=new_amount_of_package)
			bloodGroup = instance.bloodGroup
			package = instance.package
			bloodstock = BloodStock.objects.filter(bloodGroup=bloodGroup).last()
			if bloodstock:
				new_amount_of_package = int(bloodstock.amount_of_package)+int(package)
				bloodstock.amount_of_package=new_amount_of_package
				print("package:",package)
				print("bloodstock.amount_of_package:",bloodstock.amount_of_package)
				print("new_amount_of_package:",new_amount_of_package)
				bloodstock.save()
			else:
				bloodstock = BloodStock.objects.create(bloodGroup=bloodGroup,amount_of_package=package)
			instance.save()
			messages.success(request, f'Dadus Doasaun husi doador {doasaunData.doador.firstname} {doasaunData.doador.lastname} altera ho Susesu.')
			return redirect('doador-detail-doasaun',doasaunData.doador.hashed)
	else:	
		form = DoadorBloodPackageForm(instance=doasaunData)
	context ={
		"group":group,
		"title":f"Altera Dadus Doasaun husi doador {doasaunData.doador.firstname} {doasaunData.doador.lastname}",
		"form":form,
		"page":"form",
		"active_doador":"active",
	}
	return render(request, "doador_bloodbank/formDoasaun.html",context)

@login_required
@allowed_users(allowed_roles=['admin','ubloodbank'])
def deleteDoasaun(request,hashid):
	doadorData = get_object_or_404(DoadorBloodPackage,hashed=hashid)
	returnbloodstock = BloodStock.objects.filter(bloodGroup=doadorData.bloodGroup).last()
	returnbloodstock.amount_of_package=(returnbloodstock.amount_of_package-doadorData.package)
	returnbloodstock.save()
	name = doadorData.doador.firstname + " "+doadorData.doador.lastname
	doadorData.delete()
	messages.error(request, f'Dadus doasaun husi Doador {name} hamoos ho Susesu.')
	return redirect('doador-detail-doasaun',doadorData.doador.hashed)
