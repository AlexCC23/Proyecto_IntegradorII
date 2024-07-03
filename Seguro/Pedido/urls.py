from django.urls import path, include
from rest_framework import routers
from Pedido import views

router = routers.DefaultRouter()
router.register(r'',views.PedidoView)

urlpatterns = [
    path('Pedido/', include(router.urls)),
    path('PedidoPrioridad/<fec>/<prio>/<cond>/<sta>',views.PedidoForPrioridadView.as_view({'get':'list'})),
    path('PedidoConductor/<fec>/<prio>/<cond>',views.PedidoForConductor.as_view({'get':'list'})),
    path('PedidoReceta/<est>/<rec>',views.PedidoForReceta.as_view({'get':'list'})),
    path('add-password/', views.AddPasswordToPdf.as_view(), name='add-password'),
    path('send-email/', views.SendEmailView.as_view(), name='send-email'),
]