from rest_framework.viewsets import ModelViewSet

from user.serializers import UserSerializer
from user.models import User


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        from user.utils import load_from_json
        from user.models import User
        # users = load_from_json('user/fixtures/users.json')
        # for user in users:
        #     created_user = User(
        #         username=user['username'],
        #         first_name=user['first_name'],
        #         last_name=user['last_name'],
        #         email=user['email'],
        #         is_active=user['is_active'],
        #         is_staff=user['is_staff'],
        #         is_superuser=user['is_superuser'],
        #     )
        #     created_user.set_password(user['password'])
        #     created_user.save()
        return super().list(request, *args, **kwargs)
