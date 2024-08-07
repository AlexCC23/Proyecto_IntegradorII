from django.urls import path, include
from rest_framework import routers
from RecetaMedicina import views

router = routers.DefaultRouter()
router.register(r'',views.RecetaMedicinaView,'RecetaMedicina')

urlpatterns = [
    path('RecetaMedicina/', include(router.urls)),
    path('RecetaDetalle/<rec>/',views.RecetaDetalleView.as_view({'get':'list'})), 
]
