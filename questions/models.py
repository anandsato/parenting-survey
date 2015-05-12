from django.db import models

# Create your models here.


class Question(models.Model):
	title = models.CharField(max_length = 200, blank = False, null = False)
	text = models.TextField(blank = False, null = False)
	order = models.IntegerField(default = 0)
	min_value = models.IntegerField(default = 1)
	max_value = models.IntegerField(default = 1)
	multiplier = models.DecimalField(default = 0.5, max_digits=5, decimal_places=2)

	def __unicode__(self):
		return "Question #" + str(self.order) + ": " + self.title
