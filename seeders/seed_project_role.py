import sys
import os
import django
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management.settings')
django.setup()

from project_members.models import ProjectRole

def run():
    project_roles = ['Owner', 'Project-Manager', 'Team-Lead', 'Team-Member']
    role_objs = {}
    for name in project_roles:
        role, _ = ProjectRole.objects.get_or_create(name=name)
        role_objs[name] = role
    print("✅ Project roles seeded.")