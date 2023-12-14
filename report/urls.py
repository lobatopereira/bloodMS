from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/report/b/tabular/',views.BReportDashTabular, name="b-report-dash-tabular"),
	

	path('dashboard/report/e/tabular/',views.EReportDashTabular, name="e-report-dash-tabular"),
]	