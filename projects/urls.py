from django.urls import path, include
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('create-project/', ProjectCreateView.as_view(), name='project-create'),
    path('show-project/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
    path('update-project/<int:id>/', ProjectUpdateView.as_view(), name='project-update'),
    path('delete-project/<int:id>/', ProjectDeleteView.as_view(), name='project-delete'),
]