"""gec_rikolto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from modulo_gerencia.views import *
from monitoreo_indicadores.views import *


admin.site.site_header = "Administración GEC"
admin.site.site_title = "Administración GEC"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('xls/', save_as_xls, name='xls'),
    path('', index),
    path('indicadores-objetivo/<int:id>/', indicadores_objetivo, name='indicadores-objetivo'),
    path('indicadores-efectos/<int:id>/', indicadores_efectos, name='indicadores-efectos'),
    path('indicadores-productos/<int:id>/', indicadores_productos, name='indicadores-productos'),

    #ajax admin
    path('ajax/admin/efecto/', efecto_admin, name='efecto-admin'),
    path('ajax/admin/producto/', producto_admin, name='producto-admin'),
]
