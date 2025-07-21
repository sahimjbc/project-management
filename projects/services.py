from .repository import ProjectRepository

class ProjectService:
    @staticmethod
    def list_projects():
        return ProjectRepository.list_projects()
    
    @staticmethod
    def get_project_by_id(id):
        return ProjectRepository.get_project_by_id(id)

    @staticmethod
    def create_project(**data):
        return ProjectRepository.create_project(**data)
    
    @staticmethod
    def update_project(project, **data):
        return ProjectRepository.update_project(project, **data)
    
    @staticmethod
    def delete_project(project):
        return ProjectRepository.delete_project(project)