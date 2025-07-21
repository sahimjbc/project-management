from rest_framework import serializers
from .models import User
from roles.models import Role

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone', 'is_verified']

class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, required=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        source='role',
        write_only=True,
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'role_id']
