from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.db import models

DAYS_OF_WEEK = (
	(0, 'Monday'),
	(1, 'Tuesday'),
	(2, 'Wednesday'),
	(3, 'Thursday'),
	(4, 'Friday'),
	(5, 'Saturday'),
	(6, 'Sunday'),
)

class Schedule(models.Model):
	user = models.ForeignKey(User, primary_key=True)

	def __unicode__(self):
		return unicode(self.user) 

class Entry(models.Model):
	schedule = models.ForeignKey(Schedule)
	day = models.IntegerField(choices=DAYS_OF_WEEK)
	class_name = models.CharField(max_length=7)
	start = models.TimeField("From")
	end = models.TimeField("To")

	def __unicode__(self):
		return unicode(self.schedule)

	@staticmethod
	def get_objects_by_day(day, schedule=None):
		entries_by_day = []
		entries = Entry.objects.all()
		for entry in entries:
			if schedule == None:
				if entry.day==day:
					entries_by_day.append(entry)
			else:
				if entry.day==day and entry.schedule==schedule:
					entries_by_day.append(entry)
		return entries_by_day
