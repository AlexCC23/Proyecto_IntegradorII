from django.urls import path, include
from rest_framework import routers
from Guia import views

router = routers.DefaultRouter()
router.register(r'',views.GuiaView)

urlpatterns = [
    path('Guia/', include(router.urls)),
    path('GuiaPedido/<pedi>',views.GuiaForPedidoView.as_view({'get':'list'})),
]