from .services import ProjectMemberService
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import ProjectMemberListSerializer, ProjectMemberDetailSerializer, ProjectMemberAssignSerializer, ProjectMemberUnassignSerializer
from users.permissions import HasMenuPermission
class ProjectMemberListView(generics.ListAPIView):
    serializer_class = ProjectMemberListSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'project_members'
        self.action = 'view'
        return super().get_permissions()

    def get_queryset(self):
        return ProjectMemberService.list_project_members()
class ProjectMemberDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectMemberDetailSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'project_members'
        self.action = 'view'
        return super().get_permissions()

    def get_object(self):
        member_id = self.kwargs.get('id')
        return ProjectMemberService.get_project_member_by_id(member_id)
class ProjectMemberAssignView(generics.CreateAPIView):
    serializer_class = ProjectMemberAssignSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'project_members'
        self.action = 'assign'
        return super().get_permissions()

    def perform_create(self, serializer):
        project_id = serializer.validated_data['project_id']
        user_id = serializer.validated_data['user_id']
        self.project_member = ProjectMemberService.assign_project_member(project_id, user_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(ProjectMemberDetailSerializer(self.project_member).data, status=status.HTTP_201_CREATED)
class ProjectMemberUnassignView(generics.DestroyAPIView):
    serializer_class = ProjectMemberUnassignSerializer
    permission_classes = [permissions.IsAuthenticated, HasMenuPermission]

    def get_permissions(self):
        self.menu = 'project_members'
        self.action = 'unassign'
        return super().get_permissions()

    def perform_destroy(self, instance):
        project_id = instance.project_id
        user_id = instance.user_id
        ProjectMemberService.unassign_project_member(project_id, user_id)

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)