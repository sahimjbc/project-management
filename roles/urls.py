from django.urls import path
from .views import RoleCreateView, RoleDetailView, RoleListView, RoleUpdateView, RoleDeleteView

urlpatterns = [
    path('create-role/', RoleCreateView.as_view(), name='create-role'),
    path('show-role/<int:id>/', RoleDetailView.as_view(), name='show-role'),
    path('update-role/<int:id>/', RoleUpdateView.as_view(), name='update-role'),
    path('delete-role/<int:id>/', RoleDeleteView.as_view(), name='delete-role'),
    path('', RoleListView.as_view(), name='role-list'),
]