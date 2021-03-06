from django.contrib.auth.models import User
from django.contrib.auth import login
from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from blogengine.models import Post

# Create your tests here.

class PostTest(TestCase):
	def test_create_post(self):
		# Create the post
		post = Post()

		# Set the attributes
		post.title = 'My first post'
		post.text = 'This is my first blog post'
		post.pub_date = timezone.now()

		# Save post
		post.save()

		# Chekc we can find it
		all_posts = Post.objects.all()
		self.assertEquals(len(all_posts), 1)
		only_post = all_posts[0]
		self.assertEquals(only_post, post)

		# Check attributes
		self.assertEquals(only_post.title, 'My first post')
		self.assertEquals(only_post.text, 'This is my first blog post')
		self.assertEquals(only_post.pub_date.day, post.pub_date.day)
		self.assertEquals(only_post.pub_date.month, post.pub_date.month)
		self.assertEquals(only_post.pub_date.year, post.pub_date.year)
		self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
		self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
		self.assertEquals(only_post.pub_date.second, post.pub_date.second)

class AdminTest(LiveServerTestCase):
    def setUp(self):
	    self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
	    # user.save()s


    def test_login(self):
        # Create client
        c = Client()

        # Get login page
        response = c.get('/admin/', follow=True)

        # Check response code
        self.assertEquals(response.status_code, 200)

        # print(response)	

        # Check 'Log in' in response
        self.assertTrue(b'Log in' in response.content)

        # Log the user in
        Check = c.login(username='john', password="johnpassword")
        print(Check)
        self.assertTrue(Check)	
        c.force_login(self.user)

        # Check response code
        response = c.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)

        print(response.content)

        # Check 'Log out' in response
        self.assertTrue(b'Log out' in response.content)


		