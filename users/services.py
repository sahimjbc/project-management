from .models import User
from .repository import UserRepository

class UserService:
    @staticmethod
    def list_users():
        return UserRepository.list_users()

    @staticmethod
    def get_user_by_username(username):
        return UserRepository.get_user_by_username(username)
    
    @staticmethod
    def get_user_by_id(id):
        return UserRepository.get_user_by_id(id)
    
    @staticmethod
    def create_user(data):
        user = UserRepository.create_user(**data)
        return user
    
    @staticmethod
    def update_user(user, data):
        return UserRepository.update_user(user, **data)
    
    @staticmethod
    def delete_user(user):
        return UserRepository.delete_user(user)
        