from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def lhassa(request):
	return render(request, 'pages/lhassa.html')

def croquettes(request):
	return render(request, 'pages/croquettes.html')

def handler404(request):
	return render(request, 'errors/404.html', {}, status = 404 ) 

def handler500(request):
	return render(request, 'errors/404.html', {}, status = 500 ) 