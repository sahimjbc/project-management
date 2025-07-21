from .views import ProjectMemberListView, ProjectMemberDetailView, ProjectMemberAssignView, ProjectMemberUnassignView
from django.urls import path

urlpatterns = [
    path('', ProjectMemberListView.as_view(), name='project_member_list'),
    path('<int:id>/', ProjectMemberDetailView.as_view(), name='project_member_detail'),
    path('assign/', ProjectMemberAssignView.as_view(), name='project_member_assign'),
    path('unassign/', ProjectMemberUnassignView.as_view(), name='project_member_unassign'),
]