from django.urls import path
from . import views
urlpatterns = [
	path('list/',views.EnfermariaList, name="EnfermariaList"),
	path('adisiona/',views.addEnfermaria, name="addEnfermaria"),
	path('altera/enfermaria/<str:id>',views.updateEnfermaria, name="updateEnfermaria"),
	path('delete/enfermaria/<str:id>',views.deleteEnfermaria, name="deleteEnfermaria"),

	# request
	path('list/blood-request/',views.EBloodRequestList, name="e-blood-request-list"),
	path('list/blood-group-request/<str:idGrupuRan>',views.EBloodGroupRequestList, name="e-blood-group-request-list"),
	path('list/blood-request/detail/<str:bloodRequestID>',views.EBloodRequestResponseDetail, name="e-blood-request-response-detail"),
	path('list/blood-request/add/',views.EBloodRequestAdd, name="e-blood-request-add"),
	path('list/blood-request/response/use/<str:bloodRequestResponseID>',views.EBloodRequestResponseUse, name="use-response-blood-package"),
	path('list/blood-request/response/un-use/<str:bloodRequestResponseID>',views.EBloodRequestResponseUnUse, name="un-use-response-blood-package"),
	# response
	path('list/blood-request/response/<str:bloodRequestID>',views.BBloodRequestResponseAdd, name="b-blood-request-response-add"),
	path('detail/blood-request/response/<str:bloodRequestID>',views.BBloodRequestResponseDetail, name="b-blood-request-response-detail"),
	path('delete/blood-request/response/<str:bloodRequestID>',views.BBloodRequestResponseDelete, name="b-blood-request-response-delete"),
	path('konfirma/blood-request/response/<str:bloodRequestID>',views.BBloodRequestResponseKonfirma, name="b-blood-request-response-confirm"),
	
	path('list/blood-request/responded/true/',views.ListBloodRequestRespondTrue, name="b-list-blood-request-respond-true"),
	path('list/blood-group-request/responded/true/<str:idGrupuRan>',views.ListBloodGroupRequestRespondTrue, name="b-list-blood-group-request-respond-true"),
	
	path('list/blood-request/lock/<str:hashid>',views.LockBloodRequest, name="e-blood-request-lock"),
	path('list/blood-request/unlock/<str:hashid>',views.UnLockBloodRequest, name="e-blood-request-unlock"),
	path('list/blood-request/send/<str:hashid>',views.SendBloodRequest, name="e-blood-request-send"),

	
]
