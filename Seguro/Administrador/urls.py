from django.urls import path, include
from rest_framework import routers
from Administrador import views

router = routers.DefaultRouter()
router.register(r'Administrador',views.AdministradorView)

urlpatterns = [
    path('Administrador/', include(router.urls))
]
