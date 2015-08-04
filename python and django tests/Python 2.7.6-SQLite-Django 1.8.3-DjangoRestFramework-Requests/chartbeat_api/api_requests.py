"""
Get data from ChartBeat's test API in order to have some data to test
in the local DB. After getting this data I call my API and make a POST
to the DB in order to create new hostname and its pages.
"""


__author__ = 'RZapata'

import os

import django
from rest_framework import status
import requests


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chartbeat_api.settings')
django.setup()


from concurrents_increase.models import Domain, Page



# TODO: create a list of hostnames and iterate through each one of them
# in order to put all the data in just one run in the DB.
HOSTNAME = 'gizmodo.com'
LIMIT_PER_CALL = '50'

# Creating a domain through my API first
my_api = r"http://localhost:8000/v4/toppages/hostname/create"
# params for my api. The string part of the url is for the Django URLField validator.
my_parameters = {'domain_name': "http://www."+HOSTNAME}
# making a POST call
pos_request = requests.post(my_api, data=my_parameters)

get_request = requests.get(my_api)

#print get_request.json()

print pos_request.status_code, type(pos_request.status_code)

if pos_request.status_code == status.HTTP_201_CREATED:

    # params for calling ChartBeat's API
    payload = {'host': HOSTNAME, 'limit': LIMIT_PER_CALL, 'apikey': '317a25eccba186e0f6b558f45214c0e7'}

    # test url
    api = r"http://api.chartbeat.com/live/toppages/"

    # getting the response from ChartBeat
    r = requests.get(api, payload)

    # Getting the domain's id from Django's models
    host = Domain.objects.filter(domain_name__icontains=HOSTNAME)[0]

    # Parsing through all the data
    # and saving to the Page model in the DB
    for each_page in r.json():
        try:
            p = Page.objects.get_or_create(i=each_page['i'].encode('utf-8'), path=each_page['path'].encode('utf-8'), visitors=each_page['visitors'], change=0, domain_id=host)[0]
            p.save()
        except UnicodeEncodeError:
            print 'i', "-->", each_page['i']
            print 'path', "-->", each_page['path']
            print 'visitors', "-->", each_page['visitors']
else:
    pos_request.raise_for_status()


