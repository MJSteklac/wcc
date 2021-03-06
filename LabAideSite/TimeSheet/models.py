from django.contrib.auth.models import User
from django.db import models

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
	is_project = models.BooleanField("Is it a project?")
	
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
