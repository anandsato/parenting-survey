
from django.contrib import admin

from .models import Submission

class SubmissionAdmin(admin.ModelAdmin):
	class Meta:
		model = Submission

admin.site.register(Submission, SubmissionAdmin)