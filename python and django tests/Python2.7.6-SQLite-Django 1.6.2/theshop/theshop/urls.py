from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^shoppinglists/', include('shoppinglists.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       
)
