from __future__ import division
import json
from django.shortcuts import render
from questions.models import Question
from submissions.models import Submission



# Create your views here.

def smart_truncate(content, length=90, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return content[:length].rsplit(' ', 1)[0]+suffix


def profile(request):
	if request.method == "POST":
		data = dict(request.POST)
		data = data["data"][0]
		data = json.loads(data)
		# print type(data)
		# if isinstance(data, dict):
		# 	print True

		# print data.keys()

		s = Submission()
		s.name = data['name']
		s.submitted_data = json.dumps(data["json"])
		s.total_score = data['total_score']
		s.save()

	q = Question.objects.all().order_by('order')
	print len(q)
	template = "base.html"
	context = { "questions": q} #"form": form, "image_form": image_form
	return render(request, template, context)

def thank_you(request):
	template = "thank-you.html"
	context = {} #"form": form, "image_form": image_form
	return render(request, template, context)


def results(request):
	subs= Submission.objects.all()
	qs = Question.objects.all().order_by('order')
	all_results = []
	for q in qs:
		answers = []
		for s in subs:
			data = json.loads(s.submitted_data)
			number = data.get(str(q.id),None)
			if number != None:
				answers.append(int(number))
		results = []
		results.append(q.order)
		results.append(smart_truncate(q.text))
		results.append(sum(answers) / len(answers))
		results.append(len(answers))
		all_results.append(results)
	print all_results
	template = "results.html"
	context = {"results": all_results, "submissions": subs} #"form": form, "image_form": image_form
	return render(request, template, context)




