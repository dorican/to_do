from rest_framework.viewsets import ModelViewSet

from backend.user.serializers import UserSerializer
from backend.user.models import User


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
