from django.urls import path, include
from rest_framework import routers
from Pedido import views

router = routers.DefaultRouter()
router.register(r'',views.PedidoView)

urlpatterns = [
    path('Pedido/', include(router.urls)),
    path('PedidoPrioridad/<fec>/<prio>/<cond>',views.PedidoForPrioridadView.as_view({'get':'list'})),
]