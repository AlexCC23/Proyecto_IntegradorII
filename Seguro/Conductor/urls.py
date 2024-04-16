from django.urls import path, include
from rest_framework import routers
from Conductor import views

router = routers.DefaultRouter()
router.register(r'Conductor',views.ConductorView)

urlpatterns = [
    path('Conductor/', include(router.urls))
]