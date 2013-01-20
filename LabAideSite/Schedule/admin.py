from Schedule.models import Schedule, Entry
from django.contrib import admin

class EntryInline(admin.StackedInline):
	model = Entry
	extra = 1

class ScheduleAdmin(admin.ModelAdmin):
	inlines = [EntryInline]

admin.site.register(Schedule, ScheduleAdmin)
