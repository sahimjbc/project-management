from .services import PermissionService
from .serializers import PermissionSerializer, PermissionCreateSerializer, PermissionUpdateSerializer, PermissionDeleteSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.permissions import HasMenuPermission

class PermissionListView(generics.ListAPIView):
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'permissions'
        self.action = 'view'
        return super().get_permissions()

    def get_queryset(self):
        return PermissionService.list_permissions()
class PermissionCreateView(generics.CreateAPIView):
    serializer_class = PermissionCreateSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'permissions'
        self.action = 'create'
        return super().get_permissions()

    def perform_create(self, serializer):
        self.permission = PermissionService.create_permission(**serializer.validated_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(PermissionSerializer(self.permission).data, status=status.HTTP_201_CREATED)
class PermissionDetailView(generics.RetrieveAPIView):
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'permissions'
        self.action = 'view'
        return super().get_permissions()

    def get_object(self):
        permission_id = self.kwargs.get('id')
        return PermissionService.get_permission_by_id(permission_id)
class PermissionUpdateView(generics.UpdateAPIView):
    serializer_class = PermissionUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'permissions'
        self.action = 'edit'
        return super().get_permissions()

    def get_object(self):
        permission_id = self.kwargs.get('id')
        return PermissionService.get_permission_by_id(permission_id)

    def perform_update(self, serializer):
        permission = self.get_object()
        PermissionService.update_permission(permission, **serializer.validated_data)
        return Response(PermissionSerializer(permission).data, status=status.HTTP_200_OK)
class PermissionDeleteView(generics.DestroyAPIView):
    serializer_class = PermissionDeleteSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'permissions'
        self.action = 'delete'
        return super().get_permissions()

    def get_object(self):
        permission_id = self.kwargs.get('id')
        return PermissionService.get_permission_by_id(permission_id)

    def perform_destroy(self, instance):
        PermissionService.delete_permission(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)