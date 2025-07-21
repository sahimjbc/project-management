from .services import RoleService
from .serializers import RoleSerializer, RoleCreateSerializer, RoleUpdateSerializer, RoleDeleteSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.permissions import HasMenuPermission

class RoleListView(generics.ListAPIView):
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'roles'
        self.action = 'view'
        return super().get_permissions()

    def get_queryset(self):
        return RoleService.list_roles()
class RoleCreateView(generics.CreateAPIView):
    serializer_class = RoleCreateSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'roles'
        self.action = 'create'
        return super().get_permissions()

    def perform_create(self, serializer):
        self.role = RoleService.create_role(**serializer.validated_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(RoleSerializer(self.role).data, status=status.HTTP_201_CREATED)

class RoleDetailView(generics.RetrieveAPIView):
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'roles'
        self.action = 'view'
        return super().get_permissions()

    def get_object(self):
        role_id = self.kwargs.get('id')
        return RoleService.get_role_by_id(role_id)  

class RoleUpdateView(generics.UpdateAPIView):
    serializer_class = RoleUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'roles'
        self.action = 'edit'
        return super().get_permissions()

    def get_object(self):
        role_id = self.kwargs.get('id')
        return RoleService.get_role_by_id(role_id)

    def perform_update(self, serializer):
        role = self.get_object()
        RoleService.update_role(role, **serializer.validated_data)

class RoleDeleteView(generics.DestroyAPIView):
    serializer_class = RoleDeleteSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'roles'
        self.action = 'delete'
        return super().get_permissions()

    def get_object(self):
        role_id = self.kwargs.get('id')
        return RoleService.get_role_by_id(role_id)

    def perform_destroy(self, instance):
        RoleService.delete_role(instance)