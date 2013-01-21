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
