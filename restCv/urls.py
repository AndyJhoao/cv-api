from django.urls import path, include
from rest_framework import routers
from restCv import views

router = routers.DefaultRouter()
router.register(r'restCv', views.restView)

urlpatterns = [
    path('/', include(router.urls))
]
