from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emmaBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'blog.views.index', name='home'),
	url(r'^posts/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$', ),
)
