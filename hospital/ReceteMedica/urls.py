from django.urls import path, include
from rest_framework import routers
from ReceteMedica import views

#generamos las rutas de get post put delete por defecto 
router = routers.DefaultRouter()
router.register(r'',views.RecetaView,'RecetaMedica')#indico a que API estoy llamando con los get, post, etc

urlpatterns = [
    path('RecetaMedica/', include(router.urls)) # crear la url para cada metodo
]




