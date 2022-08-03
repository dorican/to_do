from rest_framework.viewsets import ModelViewSet

from user.serializers import UserSerializer
from user.models import User


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
