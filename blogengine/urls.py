from django.conf.urls import url

from . import views

app_name = 'blogengine'

urlpatterns = [
	url(r'^$', views.home, name='home1'),
	url(r'^home/$', views.IndexView.as_view(), name='home'),
	url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'index/$', views.index, name='index'),

	# url(r'^home/$', views.home, name='home'),
	
    # url(r'^(?P<poll_id>[0-9]+)/$', views.PostView.as_view(), name='detail'),
]

