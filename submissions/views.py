
import json
from django.shortcuts import render
from questions.models import Question
from submissions.models import Submission


# Create your views here.


def profile(request):
	if request.method == "POST":
		data = request.POST
		print data
		s = Submission()
		s.name = data['name']
		s.submitted_data = json.dumps(data)
		s.total_score = data['total_score']
		s.save()



	q = Question.objects.all().order_by('order')
	print len(q)
	template = "profile.html"
	context = { "questions": q} #"form": form, "image_form": image_form
	return render(request, template, context)
