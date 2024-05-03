"""
URL configuration for Seguro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Seguro/', include('Asegurado.urls')),
    path('Seguro/', include('Administrador.urls')),
    path('Seguro/', include('Conductor.urls')),
    path('Seguro/', include('Kardex.urls')),
    path('Seguro/', include('Pedido.urls')),
    path('Seguro/', include('Receta.urls')),
    path('Seguro/', include('Medicina.urls')),
    path('Seguro/', include('Receta_Medicina.urls')),
]
