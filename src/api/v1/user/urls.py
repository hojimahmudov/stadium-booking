from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet, PermissionViewSet, RolePermissionView

router = DefaultRouter()
router.register(r"role", RoleViewSet)
router.register(r"permission", PermissionViewSet)
router.register(r"", UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('role/<int:pk>/permission/', RolePermissionView.as_view())
]
