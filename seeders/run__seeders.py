import sys
import os
import django

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management.settings')
django.setup()

from seeders import seed_roles_permissions, seed_project_role, seed_users

def run_all_seeders():
    print("🚀 Starting all seeders...")

    try:
        print("🔹 Seeding roles and permissions...")
        seed_roles_permissions.run()
    except Exception as e:
        print(f"❌ Error in seed_roles_permissions: {e}")

    try:
        print("🔹 Seeding project roles...")
        seed_project_role.run()
    except Exception as e:
        print(f"❌ Error in seed_project_role: {e}")

    try:
        print("🔹 Seeding users...")
        seed_users.run()
    except Exception as e:
        print(f"❌ Error in seed_users: {e}")

    print("✅ All seeders completed.")

if __name__ == '__main__':
    run_all_seeders()
