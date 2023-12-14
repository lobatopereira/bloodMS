"""bloodMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('', include('main.urls')),
    path('custom/', include('custom.urls')),
    path('users/', include('users.urls')),
    path('enfermaria/', include('enfermaria.urls')),
    path('blood-stock/', include('bloodstock.urls')),
    path('donate/', include('doador.urls')),
    path('pasiente/', include('patient.urls')),
    path('charts/', include('charts.urls')),
    path('report/', include('report.urls')),
    path('notification/', include('notification.urls')),
    path('api/notification/', include('notification.api.urls')),
    path('api/', include('api.urls')),
    path('summernote/', include('django_summernote.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "SISTEMA INFORMASAUN STOCK RAN - SUPER USER"
admin.site.site_title = "SISTEMA INFORMASAUN STOCK RAN - SUPER USER"
admin.site.index_title = "Portal Super User"