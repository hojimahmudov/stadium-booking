from django.urls import path, include
from .views import StadiumViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stadium', StadiumViewSet)

urlpatterns = [
    path('my/', include(router.urls))
]
