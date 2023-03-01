from django.contrib.auth.models import User
from django.db import models

from core.models import Group


class Task(models.Model):
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=500, verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name='Изображение', blank=True)
    time_created = models.DateTimeField(auto_created=True, verbose_name="Время создания")
    user_created = models.ForeignKey(User, verbose_name="Создатель задачи", on_delete=models.DO_NOTHING)
    deadline = models.DateTimeField(verbose_name="Крайний срок")
    is_done = models.BooleanField(verbose_name="Выполнено", default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['time_created']

    def __str__(self):
        return self.title


class SubTask(models.Model):
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=500, verbose_name="Описание", blank=True)
    time_created = models.DateTimeField(auto_created=True, verbose_name="Время создания")
    user_created = models.ForeignKey(User, verbose_name="Создатель задачи", on_delete=models.DO_NOTHING)
    deadline = models.DateTimeField(verbose_name="Крайний срок")
    is_done = models.BooleanField(verbose_name="Выполнено", default=False)
    parent_task = models.ForeignKey(Task, verbose_name="Родительская задача", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'
        ordering = ['id']

    def __str__(self):
        return f'{self.title} ({self.parent_task})'


class ResponsibleOnTask(models.Model):
    task = models.ForeignKey(Task, verbose_name="Задача", on_delete=models.CASCADE)
    responsible_user = models.ForeignKey(User, verbose_name="Ответственный пользователей", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответственный по задаче'
        verbose_name_plural = 'Ответственные по задачам'
        ordering = ['id']

    def __str__(self):
        return f'{self.task} - {self.responsible_user.username}'


