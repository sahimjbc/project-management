from .models import Permission, Menu, Action
from roles.models import Role
from rest_framework import serializers

class PermissionSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name', read_only=True)
    menu = serializers.CharField(source='menu.name', read_only=True)
    action = serializers.CharField(source='action.name', read_only=True)

    class Meta:
        model = Permission
        fields = ['id', 'role', 'menu', 'action']
class PermissionCreateSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        source='role',
        write_only=True,
        required=True
    )
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(),
        source='menu',
        write_only=True,
        required=True
    )
    action_id = serializers.PrimaryKeyRelatedField(
        queryset=Action.objects.all(),
        source='action',
        write_only=True,
        required=True
    )

    class Meta:
        model = Permission
        fields = ['role_id', 'menu_id', 'action_id']

class PermissionUpdateSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        source='role',
        write_only=True,
        required=False
    )
    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(),
        source='menu',
        write_only=True,
        required=False
    )
    action_id = serializers.PrimaryKeyRelatedField(
        queryset=Action.objects.all(),
        source='action',
        write_only=True,
        required=False
    )

    class Meta:
        model = Permission
        fields = ['role_id', 'menu_id', 'action_id']
        read_only_fields = ['id']

class PermissionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id']

    def validate(self, attrs):
        if not self.instance:
            raise serializers.ValidationError("Permission instance does not exist.")
        return attrs

    def delete(self):
        self.instance.delete()
        return {"message": "Permission deleted successfully."}