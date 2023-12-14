from django.db import models
from bloodstock.models import BloodGroup
from custom.models import Municipality,AdministrativePost,Village
from django.contrib.auth.models import User

# Create your models here.
class Doador(models.Model):
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True,related_name="municipality",blank=True, verbose_name="Munisipiu")
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE, null=True,related_name="administrativepost",blank=True, verbose_name="Postu Administrativu")
	village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True,related_name="village",blank=True, verbose_name="Suku")
	firstname = models.CharField(max_length=200, null=True, verbose_name="Naran Propriu")
	lastname = models.CharField(max_length=200, null=True, verbose_name="Apelidu")
	sex = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')],max_length=4,null=True,verbose_name="Seksu")
	date_of_birth = models.DateField(null=True, verbose_name="Data Moris")
	weight = models.CharField(max_length=100,null=True,verbose_name="Todan (KG)")
	address = models.CharField(max_length=100,null=True,verbose_name="Hela Fatin")
	pressure = models.CharField(max_length=10,verbose_name="Tensaun")
	bloodGroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True,blank=True,verbose_name="Grupu Ran")
	image = models.ImageField(upload_to='doador', null=True,blank=True,verbose_name="Fotografia Doador")
	user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='user_created_doador')
	hashed = models.CharField(max_length=32, null=True)


	def __str__(self):
		template = '{0.firstname} {0.lastname} ({0.bloodGroup})'
		return template.format(self)

class DoadorBloodPackage(models.Model):
	doador = models.ForeignKey(Doador, on_delete=models.CASCADE, null=True,blank=True)
	bloodGroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True,blank=True)
	package = models.IntegerField(verbose_name="Total Pakote Ran",null=True)
	donationdate = models.DateField(auto_now_add=False, auto_now=False, blank=True,null=True)
	packageStatus = models.CharField(choices=[('Banked','Banked'),('Used','Used')],default="Banked",max_length=30,null=True,blank=True)
	typeD = models.CharField(default="Voluntariu",choices=[('Voluntariu','Voluntariu'),('Subtituisaun','Subtituisaun')],max_length=30,null=True,blank=True)
	user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='user_created_doador_bp')
	hashed = models.CharField(max_length=32, null=True)


	def __str__(self):
		template = '{0.doador}, pakote : {0.package}, data doasaun : {0.donationdate}.'
		return template.format(self)



class Substitution(models.Model):
	firstname = models.CharField(max_length=200, null=True, verbose_name="Naran Propriu")
	lastname = models.CharField(max_length=200, null=True, verbose_name="Apelidu")
	sex=models.CharField(choices=[('Mane','Mane'),('Feto','Feto')],max_length=4,null=True)
	address=models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, verbose_name="Data Moris")
	weight=models.CharField(max_length=100,null=True)
	pressure=models.CharField(max_length=10)
	bloodGroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True,blank=True)
	image = models.ImageField(upload_to='substitution', null=True,blank=True,verbose_name="Fotografia Substitution")
	user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='user_created_substitution')
	hashed = models.CharField(max_length=32, null=True)

	def __str__(self):
		template = '{0.firstname} {0.lastname} ({0.donationdate})'
		return template.format(self)


class SubstitutionBloodPackage(models.Model):
	substitution = models.ForeignKey(Substitution, on_delete=models.CASCADE, null=True,blank=True)
	bloodGroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True,blank=True)
	package = models.CharField(max_length=10)
	donationdate = models.DateField(auto_now_add=False, auto_now=False, blank=True,null=True)
	packageStatus = models.CharField(choices=[('Banked','Banked'),('Used','Used')],default="Banked",max_length=30,null=True,blank=True)
	user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='user_created_substitution_bp')
	hashed = models.CharField(max_length=32, null=True)


	def __str__(self):
		template = '{0.substitution}  ({0.donationdate}) {0.package}'
		return template.format(self)

