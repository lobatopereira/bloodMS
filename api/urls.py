from django.urls import path
from . import views

urlpatterns = [
	path('g/blood/stock/bank/', views.APIGBloodStockB.as_view(), name="api-g-blood-stock-bank"),	
	path('g/blood/enfermaria/request/', views.APIGBloodRequestEnfB.as_view(), name="api-g-blood-enfermaria-request"),	
	path('g/blood/banked/used/stock/bank/', views.APIGBloodBankedUsedStockB.as_view(), name="api-g-blood-banked-used-stock-bank"),	
	path('g/blood-banked-used-out/stock/bank/this-year/', views.APIGBloodBankedUsedOutStockThisYearB.as_view(), name="api-g-blood-banked-used-out-stock-bank-this-year"),	
	path('g/blood-banked-used-out/stock/bank/by-year/', views.APIGBloodBankedUsedOutStockByYearB.as_view(), name="api-g-blood-banked-used-out-stock-bank-by-year"),	
	path('g/patient/sex/blood-group/bank/', views.APIGPatientSexBloodGroup.as_view(), name="api-g-patient-sex-blood-group-bank"),	
]