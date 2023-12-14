from django.urls import path
from . import views
urlpatterns = [
	path('list/',views.BloodGroupList, name="BloodGroupList"),
	path('adisiona/',views.addGrupuRan, name="addGrupuRan"),
	path('altera/<str:id>',views.updateGrupuRan, name="updateGrupuRan"),
	path('delete/<str:id>',views.deleteGrupuRan, name="deleteGrupuRan"),
	
	path('total/pakote/',views.BloodStockList, name="BloodStockList"),
	
]
