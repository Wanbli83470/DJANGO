from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def lhassa(request):
	return render(request, 'pages/lhassa.html')

def croquettes(request):
	return render(request, 'pages/croquettes.html')