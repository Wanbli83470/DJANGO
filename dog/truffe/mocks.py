from django.http import Http404

class Post():
	POSTS = [
		{'id' : '1', 'title' : 'Coussinet', 'body' : "Les coussinets sont très utiles. Ils permettent au chien de marcher sur des terrains escarpés sans se faire mal."},

		{'id' : '2', 'title' : 'Truffe', 'body' : "Si la truffe de votre chien n'est pas comme d'habitude, il convient d'y prêter attention afin de s'assurer qu'il va bien et ne souffre d'aucune maladie."},

		{'id' : '3', 'title' : 'Frolic', 'body' : "gammes Frolic Complete et Croqui'Moelleux, Promos et lots Frolic, croquettes pour des repas complets et équilibrés."},

		{'id' : '4', 'title' : 'Toilletage', 'body' : "L'essor de ce marché est bien réel comme en témoignent ces chiffres : le nombre de salons de toilettage a presque doublé en 10 ans. La conséquence directe est la hausse des besoins en personnel qualifié."},
	]

	@classmethod
	def all(cls):
		return cls.POSTS

	@classmethod
	def find(cls, id):
		try :
			return cls.POSTS[int(id) - 1]

		except :
			raise Http404("Wouf, ma truffe ne connais pas la page {} ".format(id))
