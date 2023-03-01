import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from core.models import Group


class Budget(models.Model):
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Бюджет'
        verbose_name_plural = 'Бюджеты'
        ordering = ['id']

    def __str__(self):
        return f'Бюджет {self.group}'

    def get_total_income(self):
        total_income = MoneyFlow.objects.filter(
            budget=self,
            category=1
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return total_income

    def get_total_income_this_month(self):
        total_income = MoneyFlow.objects.filter(
            budget=self,
            category=1,
            date__month=datetime.date.today().month,
            date__year=datetime.date.today().year
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return total_income

    def get_total_income_this_year(self):
        total_income = MoneyFlow.objects.filter(
            budget=self,
            category=1,
            date__year=datetime.date.today().year
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return total_income

    def get_total_outgo(self):
        total_outgo = MoneyFlow.objects.filter(
            budget=self,
            category=2
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return total_outgo

    def get_total_outgo_this_month(self):
        total_outgo = MoneyFlow.objects.filter(
            budget=self,
            category=2,
            date__month=datetime.date.today().month,
            date__year=datetime.date.today().year
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return total_outgo

    def get_total_outgo_this_year(self):
        total_outgo = MoneyFlow.objects.filter(
            budget=self,
            category=2,
            date__year=datetime.date.today().year
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return total_outgo

    def get_total_flow(self):
        return self.get_total_income() - self.get_total_outgo()

    def get_total_flow_this_month(self):
        return self.get_total_income_this_month() - self.get_total_outgo_this_month()

    def get_total_flow_this_year(self):
        return self.get_total_income_this_year() - self.get_total_outgo_this_year()


class MoneyFlowCategory(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50)

    class Meta:
        verbose_name = 'Категория движения денег'
        verbose_name_plural = 'Категории движения денег'
        ordering = ['id']

    def __str__(self):
        return self.name


class MoneyFlowSubcategory(models.Model):
    moneyflow_category = models.ForeignKey(MoneyFlowCategory, verbose_name='Категория движения денег',
                                           on_delete=models.PROTECT)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=50)
    user_created = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.DO_NOTHING)
    time_created = models.DateTimeField(auto_created=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Подкатегория движения денег'
        verbose_name_plural = 'Подкатегории движения денег'
        ordering = ['id']

    def __str__(self):
        return f'{self.group} - {self.name}'


class MoneyFlow(models.Model):
    budget = models.ForeignKey(Budget, verbose_name='Бюджет', on_delete=models.CASCADE)
    category = models.ForeignKey(MoneyFlowCategory, verbose_name='Доход или расход', on_delete=models.PROTECT)
    subcategory = models.ForeignKey(MoneyFlowSubcategory, verbose_name='Категория доходов', on_delete=models.DO_NOTHING)
    amount = models.DecimalField(verbose_name='Сумма', max_digits=19, decimal_places=2)
    comment = models.TextField(verbose_name='Комментарий', max_length=500)
    date = models.DateField(verbose_name='Дата поступления')
    user_added = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Движение денег'
        verbose_name_plural = 'Движения денег'
        ordering = ['id']

    def __str__(self):
        return f'[{self.budget.group}] {self.category}, {self.subcategory} от {self.date}'
