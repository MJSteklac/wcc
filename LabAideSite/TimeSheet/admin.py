from TimeSheet.models import PayPeriod
from django.contrib import admin

class PayPeriodAdmin(admin.ModelAdmin):
	fields = ['period', 'ends_on']

admin.site.register(PayPeriod, PayPeriodAdmin)
