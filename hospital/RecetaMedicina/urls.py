from django.urls import path, include
from rest_framework import routers
from RecetaMedicina import views

router = routers.DefaultRouter()
router.register(r'RecetaMedicina',views.RecetaMedicinaView,'RecetaMedicina')

urlpatterns = [
    path('RecetaMedicina/', include(router.urls)) 
]
