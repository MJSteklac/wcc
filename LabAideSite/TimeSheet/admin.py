from TimeSheet.models import PayPeriod, Category
from django.contrib import admin

class PayPeriodAdmin(admin.ModelAdmin):
	fields = ['period', 'ends_on']

class CategoryAdmin(admin.ModelAdmin):
	fields = ['name']

admin.site.register(PayPeriod, PayPeriodAdmin)
admin.site.register(Category, CategoryAdmin)
