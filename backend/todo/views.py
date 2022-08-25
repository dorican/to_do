from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin, CreateModelMixin,
                                   DestroyModelMixin)
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from backend.todo.serializers import ProjectSerializer, ToDoSerializer
from backend.todo.models import Project, ToDo
from backend.todo.filters import ProjectFilter, ToDoFilter


class ProjectPaginator(PageNumberPagination):
    page_size = 10


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectPaginator
    filterset_class = ProjectFilter


class ToDoPaginator(PageNumberPagination):
    page_size = 20


class ToDoModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                       CreateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoPaginator
    filterset_class = ToDoFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(f'{instance} удалено')
