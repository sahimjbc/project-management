from rest_framework import serializers
from .models import Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, attrs):
        if attrs.get('end_date') and attrs['end_date'] < attrs['start_date']:
            raise serializers.ValidationError("End date cannot be before start date.")
        return attrs

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, attrs):
        if attrs.get('end_date') and attrs['end_date'] < attrs['start_date']:
            raise serializers.ValidationError("End date cannot be before start date.")
        return attrs

class ProjectDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id']

    def validate(self, attrs):
        if 'id' not in attrs:
            raise serializers.ValidationError("ID is required to delete a project.")
        return attrs