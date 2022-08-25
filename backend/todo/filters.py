from django_filters import rest_framework as filters
from backend.todo.models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ('title',)


class ToDoFilter(filters.FilterSet):
    min_date = filters.DateTimeFilter(field_name='is_created', lookup_expr='gte', input_formats=['%Y-%m-%dT%H:%M'])
    max_date = filters.DateTimeFilter(field_name='is_created', lookup_expr='lte', input_formats=['%Y-%m-%dT%H:%M'])
    is_created = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ('project', 'is_created')
