from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet

from backend.user.serializers import UserSerializer
from backend.user.models import User


class UserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                       GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
