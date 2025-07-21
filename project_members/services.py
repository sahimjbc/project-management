from .repository import ProjectMemberRepository
class ProjectMemberService:
    @staticmethod
    def list_project_members():
        return ProjectMemberRepository.list_project_members()
    
    @staticmethod
    def get_project_member_by_id(id):
        return ProjectMemberRepository.get_project_member_by_id(id)

    @staticmethod
    def assign_project_member(project_id, user_id):
        return ProjectMemberRepository.assign_project_member(project_id, user_id)
    
    @staticmethod
    def unassign_project_member(project_id, user_id):
        return ProjectMemberRepository.unassign_project_member(project_id, user_id)