from .models import Permission

class PermissionRepository:
    @staticmethod
    def list_permissions():
        return Permission.objects.all()
    
    @staticmethod
    def get_permission_by_id(id):
        return Permission.objects.filter(id=id).first()

    @staticmethod
    def create_permission(**data):
        return Permission.objects.create(**data)
    
    @staticmethod
    def update_permission(permission, **data):
        return Permission.objects.filter(id=permission.id).update(**data)
    
    @staticmethod
    def delete_permission(permission):
        return Permission.objects.filter(id=permission.id).delete()