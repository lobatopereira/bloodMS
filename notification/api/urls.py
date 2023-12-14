from django.urls import path
from . import views

urlpatterns = [
	path('badge/', views.APINotifBadge.as_view()),
	path('blood/request/', views.APINotifBloodRequest.as_view()),
	
]