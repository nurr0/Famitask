from django.contrib.auth.models import User
from django.db import models

from core.models import Group


class ShoppingList(models.Model):
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=500, verbose_name="Описание", blank=True)
    time_created = models.DateTimeField(auto_created=True, verbose_name="Время создания")
    user_created = models.ForeignKey(User, verbose_name="Создатель списка", on_delete=models.DO_NOTHING)
    is_done = models.BooleanField(verbose_name="Выполнено", default=False)

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        ordering = ['id']

    def __str__(self):
        return self.title


class ProductsInList(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="Продукт")
    shopping_list = models.ForeignKey(ShoppingList, verbose_name='Список покупок', on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='Количество', max_digits=10, decimal_places=2)
    measure = models.TextField(max_length=20, verbose_name='Мера измерения')
    is_done = models.BooleanField(verbose_name="Выполнено", default=False)

    class Meta:
        verbose_name = 'Продукт в списке'
        verbose_name_plural = 'Продукты в списке'
        ordering = ['id']

    def __str__(self):
        return f'{self.product_name}({self.shopping_list})'
