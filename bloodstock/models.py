from django.db import models

# Create your models here.
class BloodGroup(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)


class BloodStock(models.Model):
	bloodGroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True,blank=True)
	amount_of_package = models.IntegerField(null=True,blank=True)
	def __str__(self):
		template = '{0.bloodGroup} | {0.amount_of_package}'
		return template.format(self)

