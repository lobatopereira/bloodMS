from django.db import models
from doador.models import Doador,DoadorBloodPackage
from django.contrib.auth.models import User
# Create your models here.
class Enfermaria(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)


class BloodRequest(models.Model):
	patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE, null=True,blank=True)
	enfermaria = models.ForeignKey(Enfermaria, on_delete=models.CASCADE, null=True,blank=True)
	package=models.IntegerField(verbose_name="Total Pakote Ran",null=True)
	date_of_request = models.DateField(null=True, verbose_name="Data Pedidu")
	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_respond = models.BooleanField(default=False, null=True, blank=True)
	is_approved = models.BooleanField(default=False, null=True, blank=True)
	is_rejected = models.BooleanField(default=False, null=True, blank=True)
	rejected_info = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='user_created_request')
	hashed = models.CharField(max_length=32, null=True)
	def __str__(self):
		template = '{0.patient} | {0.enfermaria} | {0.date_of_request}'
		return template.format(self)


class BloodRequestResponse(models.Model):
	bloodRequest = models.ForeignKey(BloodRequest, on_delete=models.CASCADE, null=True,blank=True,related_name="bloodrequestresponse")
	doador = models.ForeignKey(DoadorBloodPackage, on_delete=models.CASCADE, null=True,blank=True)
	date_of_response = models.DateField(null=True, verbose_name="Data Pedidu")
	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_used = models.BooleanField(default=False, null=True, blank=True)
	description = models.TextField(null=True,blank=True)
	user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='user_created_response')
	hashed = models.CharField(max_length=32, null=True)
	def __str__(self):
		template = '{0.bloodRequest} | data responde :{0.date_of_response}'
		return template.format(self)





