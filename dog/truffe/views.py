from django.shortcuts import render

from .mocks import Post

def index(request):
	posts = Post.all()
	posts2 = []
	return render(request, 'truffe/index.html', {'posts' : posts,})

def show(request, id):
	posts = Post.find(id)
	return render(request, 'truffe/show.html', {'id': id, 'posts' : posts,})
