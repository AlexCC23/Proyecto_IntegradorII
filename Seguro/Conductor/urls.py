from django.urls import path, include
from rest_framework import routers
from Conductor import views

router = routers.DefaultRouter()
router.register(r'',views.ConductorView)

urlpatterns = [
    path('Conductor/', include(router.urls))
]