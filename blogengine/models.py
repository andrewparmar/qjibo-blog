from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	text = models.TextField()
	# slug = models.SlugField(max_length=40, unique=True)

	# def get_absolute_url(self):
 #        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

	def __str__(self):
		return self.title
		

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	comment_text = models.TextField()
	pub_date = models.DateTimeField()	

	def __str__(self):
		return self.name