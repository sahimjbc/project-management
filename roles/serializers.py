from rest_framework import serializers
from .models import Role
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class RoleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']

class RoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']

class RoleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id']