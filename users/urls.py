from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    UserCreateView,
    UserListView,
    UserUpdateView,
    UserDetailView,
    UserDeleteView
)

urlpatterns = [
    path('create-user/', UserCreateView.as_view(), name='create-user'),
    path('show-user/<int:id>/', UserDetailView.as_view(), name='show-user'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('update-user/<int:id>/', UserUpdateView.as_view(), name='update-user'),
    path('delete-user/<int:id>/', UserDeleteView.as_view(), name='delete-user'),
    path('', UserListView.as_view(), name='user-list'),
]
