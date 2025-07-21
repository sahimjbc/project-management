from .models import ProjectMember
from rest_framework import serializers
class ProjectMemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'user', 'role']
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'project': instance.project.name,
            'user': instance.user.username,
            'role': instance.role.name if instance.role else 'No Role'
        }

class ProjectMemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'user', 'role']
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'project': {
                'id': instance.project.id,
                'name': instance.project.name
            },
            'user': {
                'id': instance.user.id,
                'username': instance.user.username
            },
            'role': instance.role.name if instance.role else 'No Role'

        }

class ProjectMemberAssignSerializer(serializers.Serializer):
    project_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    role_id = serializers.IntegerField(required=False)

    def validate(self, data):
        if not ProjectMember.objects.filter(project_id=data['project_id'], user_id=data['user_id']).exists():
            raise serializers.ValidationError("This user is not assigned to the project.")
        return data

class ProjectMemberUnassignSerializer(serializers.Serializer):
    project_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def validate(self, data):
        if not ProjectMember.objects.filter(project_id=data['project_id'], user_id=data['user_id']).exists():
            raise serializers.ValidationError("This user is not assigned to the project.")
        return data
