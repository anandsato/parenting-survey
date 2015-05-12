from django.db import models
from jsonfield import JSONField


# Create your models here.

class Submission(models.Model):
	datetime = models.DateTimeField(auto_now_add = True)
	name = models.CharField(max_length = 255, blank = False, null = False)
	submitted_data = JSONField()


