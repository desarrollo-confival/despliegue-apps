"""crm URL Configuration

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
from core import views as core_views

urlpatterns = [

    path('admin/', admin.site.urls),

    #core vista bienvenida
    path('', core_views.home, name='home'),

    #app genero
    path('genero/', include('genero.urls')),

    #app municipio
    path('municipio/', include('municipio.urls')),

    #app perfil cliente
    path('perfil/', include('perfil.urls')),


    #app origen contacto
    path('contacto/', include('origen_contacto.urls')),

    #app tipo de documento
    path('tipo_documento/', include('tipo_documento.urls')),

    #app clase de documento
    path('clase_documento/', include('clase_documento.urls')),

    #app perfil de asesores
    path('perfil_asesor/', include('perfil_asesor.urls')),

    #app comision asesores
    path('comision/', include('comision.urls')),

    #app registro asesores
    path('asesores/', include('asesores.urls')),

    #app registro abogados
    path('abogados/', include('abogados.urls')),

]
