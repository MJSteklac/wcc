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
	period = models.IntegerField("Period", primary_key=True)
	ends_on = models.DateField("Ends on")

	def __unicode__(self):
		return unicode(self.period) 

class TimeSheet(models.Model):
	period = models.ForeignKey(PayPeriod)
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return unicode(self.period)

class Category(models.Model):
	name = models.CharField(max_length=20, primary_key=True)
	
	def __unicode__(self):
		return unicode(self.name)

class Entry(models.Model):
	timesheet = models.ForeignKey(TimeSheet)
	category = models.ForeignKey(Category)
	start = models.TimeField("From")
	end = models.TimeField("To")
	comments = models.TextField("Comments")
	date = models.DateField("Date")
	class Meta:
		ordering = ['date', 'start']

	def __unicode__(self):
		return unicode(self.timesheet)
