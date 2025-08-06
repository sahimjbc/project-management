import sys
import os
import django
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management.settings')
django.setup()

from users.models import User, Role

def run():
    try:
        admin_role = Role.objects.get(name='Super-Admin')
    except Role.DoesNotExist:
        print("'Super-Admin' role does not exist. Run seed_roles_permissions first.")
        return

    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@example.com',
            role=admin_role
        )
        print("Admin user created.")
    else:
        print("Admin user already exists.")