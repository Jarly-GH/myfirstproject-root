from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This is about page')


def home(request):
	test_get_text = request.GET['usertext']
	print(test_get_text)
	return render(request, 'home.html', {'greeting':'Hello'})