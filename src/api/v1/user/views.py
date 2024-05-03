from rest_framework import viewsets, status
from rest_framework.response import Response
from User.models import User, Role, Permission
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer, RolePermissionSerializer
from rest_framework.views import APIView
from api.v1.permissions import AdminPermission, IsStadiumOwner, IsAdminOrStadiumOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrStadiumOwner]


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class RolePermissionView(APIView):

    def patch(self, request, pk, *args, **kwargs):
        role = Role.objects.get(id=pk)

        serializer = RolePermissionSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            role.permission.set(serializer.validated_data['permission'])
            return Response(RoleSerializer(role).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
