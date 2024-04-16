from django.urls import path, include
from rest_framework import routers
from Asegurado import views

router = routers.DefaultRouter()
router.register(r'Asegurado',views.AseguradoView)

urlpatterns = [
    path('Asegurado/', include(router.urls))
]
