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

class PayPeriod(models.Model):
	period = models.IntegerField("Period")
	ends_on = models.DateField("Ends on")

	def __unicode__(self):
		return unicode(self.period) 

class TimeSheet(models.Model):
	period = models.ForeignKey(PayPeriod, primary_key=True)
	
	def __unicode__(self):
		return unicode(self.period)

class Entry(models.Model):
	timesheet = models.ForeignKey(TimeSheet)
	week = models.IntegerField("Week")
	day = models.IntegerField(choices=DAYS_OF_WEEK)
	class_name = models.CharField(max_length=7)
	start = models.TimeField("From")
	end = models.TimeField("To")
	comments = models.TextField("Comments")

	def __unicode__(self):
		return unicode(self.timesheet)
