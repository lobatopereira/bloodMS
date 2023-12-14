from django.urls import path
from . import views
urlpatterns = [
	path('lista/pedidu/ran/',views.NotifListaPediduRAN, name="NotifListaPediduRAN"),
	path('lista/pedidu/ran/grupu/<str:idGrupuRan>',views.NotifListaPediduBazeiaGrupuRAN, name="NotifListaPediduBazeiaGrupuRAN"),
	
]