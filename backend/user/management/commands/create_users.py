from django.core.management.base import BaseCommand

from backend.user.utils import load_from_json
from backend.user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = load_from_json('backend/user/fixtures/users.json')
        for user in users:
            created_user = User(
                username=user['username'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                is_active=user['is_active'],
                is_staff=user['is_staff'],
                is_superuser=user['is_superuser'],
            )
            created_user.set_password(user['password'])
            created_user.save()
