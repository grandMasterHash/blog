from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^all/$', views.allEntries, name='allEntries'),
	url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<post_id>\d+)/edit/$', views.edit, name='edit'),
	url(r'^(?P<post_id>\d+)/update/$', views.update, name='update'),
	url(r'^(?P<post_id>\d+)/delete/$', views.delete, name='delete'),
	url(r'^(?P<post_id>\d+)/comment/$', views.comment, name='comment'),
	url(r'^compose/$', views.compose, name='compose'),
	url(r'^create/$', views.create, name='create'),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^logout/$', views.userLogout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^create-user/$', views.createUser, name='createUser'),
	url(r'^login-required/$', views.loginRequired, name='loginRequired'),
)
