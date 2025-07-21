from .models import ProjectMember
class ProjectMemberRepository:
    @staticmethod
    def list_project_members():
        return ProjectMember.objects.all()
    
    @staticmethod
    def get_project_member_by_id(id):
        return ProjectMember.objects.filter(id=id).first()

    @staticmethod
    def assign_project_member(project_id, user_id):
        return ProjectMember.objects.create(project_id=project_id, user_id=user_id)
    
    @staticmethod
    def unassign_project_member(project_id, user_id):
        return ProjectMember.objects.filter(project_id=project_id, user_id=user_id).delete()