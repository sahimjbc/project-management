from .models import User

class UserRepository:
    @staticmethod
    def list_users():
        return User.objects.all()
    
    @staticmethod
    def get_user_by_username(username):
        return User.objects.filter(username=username).first()
    
    @staticmethod
    def get_user_by_id(id):
        return User.objects.filter(id=id).first()

    @staticmethod
    def create_user(**data):
        return User.objects.create(**data)
    
    @staticmethod
    def update_user(user, **data):
        return User.objects.filter(id=user.id).update(**data)
    
    @staticmethod
    def delete_user(user):
        return User.objects.filter(id=user.id).delete()

