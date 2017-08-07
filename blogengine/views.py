from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
	# template_name = 'blogengine/index.html'
	# template_name = 'blogengine/base.html'
	template_name = 'blogengine/home.html'

	def get_queryset(self):
		return Post.objects.all()


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
	# template = loader.get_template('blogengine/base.html')
	# context = {'name':'andrew'}
	# return HttpResponse("Hello Panda")
	# return HttpResponse(template.render(context, request))
	return render(request, 'blogengine/index.html')

def blog(request):
	return render(request, 'blogengine/home.html')