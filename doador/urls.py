from django.urls import path
from . import views
urlpatterns = [
	path('doador/list/',views.DoadorList, name="doador-list"),
	path('doador/list/Grupu/Ran/<str:hashid>',views.DoadorListBloodGroup, name="doador-list-bloodgroup"),
	path('doador/update/<str:hashid>',views.updateDoador, name="doador-update"),
	path('doador/delete/<str:hashid>',views.deleteDoador, name="doador-delete"),
	path('doador/detail/doasaun/<str:hashid>',views.detailDoasaunDoador, name="doador-detail-doasaun"),
	path('rejista-doasaun/banco-de-sange/',views.rejistaDoador, name="doador-add"),
	path('rejista-doasaun/doador/<str:hashid>',views.rejistaDoasaun, name="doasaun-add"),
	path('update-doasaun/doador/<str:hashid>',views.updateDoasaun, name="doasaun-update"),
	path('delete-doasaun/doador/<str:hashid>',views.deleteDoasaun, name="doasaun-delete"),
	
]
