from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название группы")
    description = models.TextField(
        max_length=600, blank=True, verbose_name="Описание")
    is_active = models.BooleanField(
        default=True, blank=False, verbose_name="Активность")
    user_created = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Создатель группы")
    date_created = models.DateField(
        auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = 'Fam'
        verbose_name_plural = 'Fams'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_users(self):
        return self.usergrouprelation_set.values_list('user', flat=True)


class UserGroupRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Связь пользователя и группы'
        verbose_name_plural = 'Связи пользователей и групп'
        ordering = ['id']
        unique_together = ('user', 'group',)

    def __str__(self):
        return f'[{self.group}] - {self.user.username}'
