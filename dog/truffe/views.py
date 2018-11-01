from django.shortcuts import render

def index(request):
	posts = [
		{'title' : 'Coussinet', 'body' : "Les coussinets sont très utiles. Ils permettent au chien de marcher sur des terrains escarpés sans se faire mal."},

		{'title' : 'Truffe', 'body' : "Si la truffe de votre chien n'est pas comme d'habitude, il convient d'y prêter attention afin de s'assurer qu'il va bien et ne souffre d'aucune maladie."},

		{'title' : 'Frolic', 'body' : "Croquettes pour chien Frolic : gammes Frolic Complete et Croqui'Moelleux, Promos et lots Frolic, croquettes pour des repas complets et équilibrés."},
	]

	posts2 = []
	return render(request, 'truffe/index.html', {'posts' : posts, 'posts2': posts2})
