from django.db import models
from bloodstock.models import BloodGroup
from enfermaria.models import Enfermaria
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
	firstname = models.CharField(max_length=200, null=True, verbose_name="Naran Propriu")
	lastname = models.CharField(max_length=200, null=True, verbose_name="Apelidu")
	sex = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')],max_length=4,null=True)
	date_of_birth = models.DateField(null=True, verbose_name="Data Moris")
	weight=models.CharField(max_length=100,null=True)
	address=models.CharField(max_length=100,null=True)
	pressure=models.CharField(max_length=10)
	bloodGroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True,blank=True)
	enfermaria = models.ForeignKey(Enfermaria, on_delete=models.CASCADE, null=True,blank=True)
	user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='user_created_patient')
	hashed = models.CharField(max_length=32, null=True)


	def __str__(self):
		template = '{0.firstname} {0.lastname} ({0.bloodGroup})'
		return template.format(self)
