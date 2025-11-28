import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

users = User.objects.all()
print(f"Total users: {users.count()}")
for user in users:
    print(f"Username: {user.username}, Active: {user.is_active}, Superuser: {user.is_superuser}")
