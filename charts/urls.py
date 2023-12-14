from django.urls import path
from . import views
urlpatterns = [
	path('dashboard/report/charts/',views.BDashCharts, name="b-dash-charts"),
	
	
	path('summury/blood-stock/',views.ChartStockRan, name="ChartStockRan"),
	
]
