from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from backend.todo.models import Project, ToDo


class ToDoSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
