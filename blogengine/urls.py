from django.conf.urls import url

from . import views

app_name = 'blogengine'

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home),
	url(r'^blog/$', views.blog),
	url(r'^$', views.IndexView.as_view(), name='index')
]

