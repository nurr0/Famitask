from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def add_user_methods_tasks(sender, instance, **kwargs):
    """
    Добавляет методы в класс User при каждом создании/обновлении объекта User
    """

    def get_active_tasks_for_user(self):
        responsible_tasks = ResponsibleOnTask.objects.filter(responsible_user=self, task__is_done=False)
        tasks = Task.objects.filter(id__in=responsible_tasks.values_list('task_id', flat=True))
        return tasks

    def get_done_tasks_for_user(self):
        responsible_tasks = ResponsibleOnTask.objects.filter(responsible_user=self, task__is_done=True)
        tasks = Task.objects.filter(id__in=responsible_tasks.values_list('task_id', flat=True))
        return tasks

    def get_all_tasks_for_user(self):
        responsible_tasks = ResponsibleOnTask.objects.filter(responsible_user=self)
        tasks = Task.objects.filter(id__in=responsible_tasks.values_list('task_id', flat=True))
        return tasks
