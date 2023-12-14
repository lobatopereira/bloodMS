from django.contrib import admin
from .models import Enfermaria,BloodRequest,BloodRequestResponse
# Register your models here.

admin.site.register(Enfermaria)
admin.site.register(BloodRequest)
admin.site.register(BloodRequestResponse)
