from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django.utils import timezone

from .models import Post, Comment

# Create your views here.

def home(request):
	print("redirecting ...")
	return redirect('/home')

class IndexView(generic.ListView):
	template_name = 'blogengine/home.html'
	def get_queryset(self):
		return Post.objects.all().order_by("-pub_date")

def post_detail(request, post_id):
	if request.method == 'POST':
		comment_post = Post.objects.get(pk=post_id)
		name = request.POST.get('name')
		email = request.POST.get('email')
		text = request.POST.get('comment')
		com = Comment(post=comment_post, name=name, email=email, comment_text=text, pub_date=timezone.now())
		com.save()
	post = get_object_or_404(Post, pk=post_id)
	comments = Comment.objects.filter(post = post_id)
	return render(request, 'blogengine/detail_post.html', {'post': post, 'comments':comments})


def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[1:5]
	template = loader.get_template('blogengine/home2.html')
	# output = ', '.join([q.text for q in latest_post_list])
	context = {'latest_post_list':latest_post_list}
	# return HttpResponse(output)
	return HttpResponse(template.render(context,request))

def vote(request, post_id):
	return HttpResponse("You just commented on post_id {}".format(post_id))


def jamba(request, post_id):
	return HttpResponse("Hello Jamba {}".format(poll_id))

# class PostView(generic.DetailView):
# 	template_name = 'blogengine/home.html'

# 	def get_queryset(self):
# 		return Post.objects.get(id__exact=2)


# def post_detail(request, post_id):
# 	try:
# 		post = Post.objects.get(pk=post_id)
# 	except Post.DoesNotExist:
# 		raise Http404("Post does not exist")
# 	return render(request, 'blogengine/detail.html', {'post': post})
	# return HttpResponse("You are looking at post {}".format(post_id))

# def home(request):
# 	# template = loader.get_template('blogengine/base.html')
# 	# context = {'name':'andrew'}
# 	# return HttpResponse("Hello Panda")
# 	# return HttpResponse(template.render(context, request))
# 	return render(request, 'blogengine/index.html')


# def home(request):
# 	return render(request, 'blogengine/home.html')