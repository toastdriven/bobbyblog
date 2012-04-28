from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


from tastypie.api import Api
from blog.api.resources import CategoryResource, PostResource
v1_api = Api()
v1_api.register(CategoryResource())
v1_api.register(PostResource())


urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),


    # Examples:
    # url(r'^$', 'bobbyblog.views.home', name='home'),
    # url(r'^bobbyblog/', include('bobbyblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
