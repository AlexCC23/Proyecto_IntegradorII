from django.urls import path, include
from rest_framework import routers
from Receta import views

router = routers.DefaultRouter()
router.register(r'',views.RecetaView)

urlpatterns = [
    path('Receta/', include(router.urls)),
    path('RecetaIDHospital/<id>',views.RecetaForIDView.as_view({'get':'list'})),
]