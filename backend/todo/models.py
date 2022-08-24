from django.db import models

from backend.user.models import User


class Project(models.Model):
    """Project`s model"""

    title = models.CharField('Название проекта', max_length=512)
    link_to_repo = models.CharField('Ссылка на репозиторий', max_length=1024, blank=True)
    user = models.ManyToManyField(User, verbose_name='Пользователи')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class ToDo(models.Model):
    """ToDo`s model"""

    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE)
    text = models.TextField('Текст заметки')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    is_created = models.DateTimeField('Создано', auto_now_add=True, auto_now=False)
    is_updated = models.DateTimeField('Обновлено', auto_now_add=False, auto_now=True)
    is_active = models.BooleanField('Активно', default=True)

