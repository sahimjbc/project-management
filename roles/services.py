from .repository import RoleRepository
class RoleService:
    @staticmethod
    def list_roles():
        return RoleRepository.list_roles()
    
    @staticmethod
    def get_role_by_name(name):
        return RoleRepository.get_role_by_name(name)
    
    @staticmethod
    def get_role_by_id(id):
        return RoleRepository.get_role_by_id(id)

    @staticmethod
    def create_role(**data):
        return RoleRepository.create_role(**data)
    
    @staticmethod
    def update_role(role, **data):
        return RoleRepository.update_role(role, **data)
    
    @staticmethod
    def delete_role(role):
        return RoleRepository.delete_role(role)