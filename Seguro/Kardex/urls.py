from django.urls import path, include
from rest_framework import routers
from Kardex import views

router = routers.DefaultRouter()
router.register(r'',views.KardexView)

urlpatterns = [
    path('Kardex/', include(router.urls))
]