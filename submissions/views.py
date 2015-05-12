from django.shortcuts import render
from questions.models import Question

# Create your views here.


def profile(request):
	q = Question.objects.all().order_by('order')
	template = "profile.html"
	context = { "questions": q} #"form": form, "image_form": image_form
	return render(request, template, context)
