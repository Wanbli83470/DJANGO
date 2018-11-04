from django.shortcuts import render

#from .mocks import Post
from .models import Post

def index(request):
	posts = Post.objects.all()
	posts2 = []
	return render(request, 'truffe/index.html', {'posts' : posts,})

def show(request, id):
	posts = Post.object.get(pk=id)
	return render(request, 'truffe/show.html', {'id': id, 'posts' : posts,})
