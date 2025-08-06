import sys
import os
import django

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management.settings')
django.setup()

from roles.models import Role
from permissions.models import Menu, Action, Permission

def run():
    roles = ['Super-Admin', 'Project-Manager', 'Team-Lead', 'Team-Member']
    role_objs = {}
    for name in roles:
        role, _ = Role.objects.get_or_create(name=name)
        role_objs[name] = role

    menus = ['users', 'dashboard', 'settings', 'projects', 'reports', 'roles', 'permissions']
    menu_objs = {}
    for name in menus:
        menu, _ = Menu.objects.get_or_create(name=name)
        menu_objs[name] = menu

    actions = ['view', 'create', 'edit', 'delete']
    action_objs = {}
    for name in actions:
        action, _ = Action.objects.get_or_create(name=name)
        action_objs[name] = action

    role_permissions = {
        'Super-Admin': {
            'users': ['view', 'create', 'edit', 'delete'],
            'roles': ['view', 'create', 'edit', 'delete'],
            'permissions': ['view', 'create', 'edit', 'delete'],
            'dashboard': ['view'],
            'settings': ['view', 'edit'],
            'projects': ['view', 'create', 'edit', 'delete'],
            'reports': ['view'],
        },
        'Project-Manager': {
            'users': ['view', 'create', 'edit'],
            'dashboard': ['view'],
            'projects': ['view', 'create', 'edit', 'delete'],
            'reports': ['view'],
        },
        'Team-Lead': {
            'users': ['view', 'edit'],
            'dashboard': ['view'],
            'projects': ['view', 'edit'],
            'reports': ['view'],
        },
    }

    for role_name, menu_actions in role_permissions.items():
        role = role_objs[role_name]
        for menu_name, actions in menu_actions.items():
            menu = menu_objs[menu_name]
            for action_name in actions:
                action = action_objs[action_name]
                Permission.objects.get_or_create(role=role, menu=menu, action=action)

    print("Roles, menus, actions, and permissions seeded.")