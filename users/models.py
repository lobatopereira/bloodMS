from django.db import models
from django.contrib.auth.models import User
from enfermaria.models import Enfermaria

class UserEnfermaria(models.Model):
	enfermaria = models.ForeignKey(Enfermaria, on_delete=models.CASCADE, null=True,blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
	firstname = models.CharField(max_length=200, null=True, verbose_name="Naran Propriu")
	lastname = models.CharField(max_length=200, null=True, verbose_name="Apelidu")
	pob = models.CharField(max_length=100, null=True, blank=True, verbose_name="Fatin Moris")
	dob = models.DateTimeField(null=True, blank=True, verbose_name="Data Moris")
	sex = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')], max_length=10, null=True, verbose_name="Sexu")
	is_active = models.BooleanField(default=True, null=True)
	image = models.ImageField(upload_to='Profile', null=True,blank=True)
	datetime = models.DateTimeField(null=True)
	user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='user_created')
	hashed = models.CharField(max_length=32, null=True)

	def __str__(self):
		template = '{0.firstname} {0.lastname} ({0.user})'
		return template.format(self)