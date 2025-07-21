from django.urls import path
from .views import PermissionListView, PermissionCreateView, PermissionDetailView, PermissionUpdateView, PermissionDeleteView

urlpatterns = [
    path('create-permission/', PermissionCreateView.as_view(), name='create-permission'),
    path('show-permission/<int:id>/', PermissionDetailView.as_view(), name='show-permission'),
    path('update-permission/<int:id>/', PermissionUpdateView.as_view(), name='update-permission'),
    path('delete-permission/<int:id>/', PermissionDeleteView.as_view(), name='delete-permission'),
    path('', PermissionListView.as_view(), name='permission-list'),
]