from django.urls import path, include
from rest_framework import routers
from Puntuacion import views

router = routers.DefaultRouter()
router.register(r'',views.PuntuacionView)

urlpatterns = [
    path('Puntuacion/', include(router.urls)),
    path('PuntuacionPedido/<pedi>',views.PuntuacionForPedidoView.as_view({'get':'list'})),
    path('PuntuacionConductor/<cond>',views.PuntuacionForConductorView.as_view({'get':'list'})),
]