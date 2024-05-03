from django.urls import path, include
from rest_framework import routers
from Medicina import views

router = routers.DefaultRouter()
router.register(r'',views.MedicinaView)

urlpatterns = [
    path('Medicina/', include(router.urls))
]