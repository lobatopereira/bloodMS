from django.contrib import admin
from .models import Doador,Substitution,DoadorBloodPackage,SubstitutionBloodPackage
# Register your models here.
admin.site.register(Doador)
admin.site.register(Substitution)
admin.site.register(DoadorBloodPackage)
admin.site.register(SubstitutionBloodPackage)
