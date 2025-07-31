from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import UserCreateSerializer, UserSerializer, UserUpdateSerializer
from .services import UserService
from .permissions import HasMenuPermission
from rest_framework.parsers import MultiPartParser, FormParser

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]
    def get_permissions(self):
        self.menu = 'users'
        self.action = 'view'
        return super().get_permissions()

    def get_queryset(self):
        return UserService.list_users()

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        self.menu = 'users'
        self.action = 'create'
        return super().get_permissions()

    def perform_create(self, serializer):
        self.user = UserService.create_user(serializer.validated_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(UserSerializer(self.user).data, status=status.HTTP_201_CREATED)

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'users'
        self.action = 'view'
        return super().get_permissions()

    def get_object(self):
        user_id = self.kwargs.get('id')
        return UserService.get_user_by_id(user_id)

class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]
    parser_classes = (MultiPartParser, FormParser)

    
    def get_permissions(self):
        self.menu = 'users'
        self.action = 'edit'
        return super().get_permissions()

    def get_object(self):
        user_id = self.kwargs.get('id')
        return UserService.get_user_by_id(user_id)

    def perform_update(self, serializer):
        user = self.get_object()
        return UserService.update_user(user, serializer.validated_data)
    
    def update(self, request, *args, **kwargs):
        print("FILES:", request.FILES)
        print("DATA:", request.data)
        return super().update(request, *args, **kwargs)
    
class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'users'
        self.action = 'delete'
        return super().get_permissions()

    def get_object(self):
        user_id = self.kwargs.get('id')
        return UserService.get_user_by_id(user_id)

    def perform_destroy(self, instance):
        UserService.delete_user(instance)
