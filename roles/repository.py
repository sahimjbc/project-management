from .models import Role

class RoleRepository:
    @staticmethod
    def list_roles():
        return Role.objects.all()
    
    @staticmethod
    def get_role_by_name(name):
        return Role.objects.filter(name=name).first()
    
    @staticmethod
    def get_role_by_id(id):
        return Role.objects.filter(id=id).first()

    @staticmethod
    def create_role(**data):
        return Role.objects.create(**data)
    
    @staticmethod
    def update_role(role, **data):
        return Role.objects.filter(id=role.id).update(**data)
    
    @staticmethod
    def delete_role(role):
        return Role.objects.filter(id=role.id).delete()