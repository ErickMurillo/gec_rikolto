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
from poa.views import *
from proyectos_financiados.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


admin.site.site_header = "Administración GEC"
admin.site.site_title = "Administración GEC"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('_nested_admin/', include('nested_admin.urls')),
    path('xls/', save_as_xls, name='xls'),
    path('', index),
    path('indicadores-objetivo/<int:id>/', indicadores_objetivo, name='indicadores-objetivo'),
    path('indicadores-efectos/<int:id>/', indicadores_efectos, name='indicadores-efectos'),
    path('indicadores-productos/<int:id>/', indicadores_productos, name='indicadores-productos'),
    path('poa/plan/<int:id>/', plan_poa, name='poa-plan'),
    path('poa/informe-semestral/<int:id>/', informe_poa, name='poa-informe'),
    path('poa/informe-anual/<int:id>/', informe_poa_anual, name='poa-informe-anual'),
    path('proyectos-financiados/plan/<int:id>/', plan_proyectos, name='plan-proyectos'),
    path('proyectos-financiados/informe/<int:id>/', informe_proyectos, name='informe-proyectos'),
    #ajax admin
    path('ajax/admin/efecto/', efecto_admin, name='efecto-admin'),
    path('ajax/admin/producto/', producto_admin, name='producto-admin'),
    #login
    path('login/', auth_views.LoginView.as_view(), {'template_name': 'login.html'}),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_base'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
