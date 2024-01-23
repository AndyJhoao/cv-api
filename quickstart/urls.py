from django.urls import path, include
from rest_framework import routers
from Quickstart import views

router = routers.DefaultRouter()
router.register(r'quickstart', views.Quickstart)

urlpatterns = [
    path('/', include(router.urls))
]
