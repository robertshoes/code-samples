__author__ = 'RZapata'


from django.conf.urls import url
from concurrents_increase import views

urlpatterns = [
    url(r'^v4/toppages/hostname$', views.concurrent_visitors_by_domain),
    url(r'^v4/toppages/hostname/create$', views.create_domain),
]
