from .models import Project

class ProjectRepository:
    @staticmethod
    def list_projects():
        return Project.objects.all()
    
    @staticmethod
    def get_project_by_id(id):
        return Project.objects.filter(id=id).first()

    @staticmethod
    def create_project(**data):
        return Project.objects.create(**data)
    
    @staticmethod
    def update_project(project, **data):
        return Project.objects.filter(id=project.id).update(**data)
    
    @staticmethod
    def delete_project(project):
        return Project.objects.filter(id=project.id).delete()