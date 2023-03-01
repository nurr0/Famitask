from django.contrib import admin

from .models import *

admin.site.register(Budget)
admin.site.register(MoneyFlowCategory)
admin.site.register(MoneyFlowSubcategory)
admin.site.register(MoneyFlow)

