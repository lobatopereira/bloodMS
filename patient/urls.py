from django.urls import path
from . import views

urlpatterns = [
	path('lista/',views.BPatientList,name="b-patient-list"),
	path('lista/Grupu/Ran/<str:hashid>',views.BPatientListBloodGroup,name="b-patient-list-bloodgroup"),
]	