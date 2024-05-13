from django.urls import path, include
from rest_framework import routers
from Receta_Medicina import views

router = routers.DefaultRouter()
router.register(r'',views.Receta_MedicinaView)

urlpatterns = [
    path('RecetaMedicina/', include(router.urls)),
    path('RecetaIDMedicina/<id_rec>',views.RecetaIDMedicinaView.as_view({'get':'list'})),
]