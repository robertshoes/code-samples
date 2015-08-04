from django.conf.urls import patterns, url

from shoppinglists import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>\d+)/$', views.show_list, name="show_list"),                   
                       
)
