from .repository import PermissionRepository
class PermissionService:
    @staticmethod
    def list_permissions():
        return PermissionRepository.list_permissions()
    
    @staticmethod
    def get_permission_by_id(id):
        return PermissionRepository.get_permission_by_id(id)

    @staticmethod
    def create_permission(**data):
        return PermissionRepository.create_permission(**data)
    
    @staticmethod
    def update_permission(permission, **data):
        return PermissionRepository.update_permission(permission, **data)
    
    @staticmethod
    def delete_permission(permission):
        return PermissionRepository.delete_permission(permission)