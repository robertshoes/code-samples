from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialcontact.views.home', name='home'),
    # url(r'^socialcontact/', include('socialcontact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/', 'people.views.list_contact'),
    url(r'^contacts?start=\d+&end=\d+/$', 'people.views.list_contact'),    
    url(r'^add_contact/', 'people.views.new_contact'),
    url(r'^search/', 'people.views.search_contact'),
    url(r'^contact_profile/(?P<contact_id>\d+)/$', 'people.views.edit_contact'),
    #url(r'^hello/', isocialcontact.urls)),
)
