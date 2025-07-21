from .services import ProjectService
from .serializers import ProjectSerializer, ProjectCreateSerializer, ProjectUpdateSerializer, ProjectDeleteSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.permissions import HasMenuPermission
class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'projects'
        self.action = 'view'
        return super().get_permissions()

    def get_queryset(self):
        return ProjectService.list_projects()
class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'projects'
        self.action = 'create'
        return super().get_permissions()

    def perform_create(self, serializer):
        self.project = ProjectService.create_project(**serializer.validated_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(ProjectSerializer(self.project).data, status=status.HTTP_201_CREATED)
class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'projects'
        self.action = 'view'
        return super().get_permissions()

    def get_object(self):
        project_id = self.kwargs.get('id')
        return ProjectService.get_project_by_id(project_id)
class ProjectUpdateView(generics.UpdateAPIView):
    serializer_class = ProjectUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'projects'
        self.action = 'edit'
        return super().get_permissions()

    def get_object(self):
        project_id = self.kwargs.get('id')
        return ProjectService.get_project_by_id(project_id)

    def perform_update(self, serializer):
        project = self.get_object()
        ProjectService.update_project(project, **serializer.validated_data)
class ProjectDeleteView(generics.DestroyAPIView):
    serializer_class = ProjectDeleteSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'projects'
        self.action = 'delete'
        return super().get_permissions()

    def get_object(self):
        project_id = self.kwargs.get('id')
        return ProjectService.get_project_by_id(project_id)

    def perform_destroy(self, instance):
        ProjectService.delete_project(instance)