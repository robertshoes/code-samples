__author__ = 'RZapata'

"""
This is a simulator for the test against the API.
It will take a random domain and will take any
of its pages and will update any of its
pages automatically with more visitors and
giving an impact in the change field.
"""

import random
import time
import os

import django
from rest_framework import status
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chartbeat_api.settings')
django.setup()


from concurrents_increase.models import Domain, Page


all_domains = Domain.objects.all()
domain_dic = {}
num_keys = 0

# Putting all domains in a dictionary of
# the type {number: domain_name}
for each_domain in all_domains:
    domain_dic[num_keys] = each_domain
    num_keys += 1

while True:
    # Generating a random number for getting a domain
    random_dom = random.randint(0, num_keys-1)
    # domain chosen
    chosen_domain = domain_dic.get(random_dom)
    print "domain selected --> " + str(chosen_domain)
    # domain object from the DB
    chosen_domain_obj = Domain.objects.filter(domain_name__icontains=chosen_domain)[0]
    # getting the pages of this domain
    related_pages = chosen_domain_obj.page_set.all()
    # choosing a random page
    random_page = random.randint(0, len(related_pages)-1)
    # updating the chosen page
    p = related_pages[random_page]
    # visitors randomly.  Negative numbers represents when users leaves
    random_visitors = random.randint(-500, 500)
    print str(random_visitors) + " Visitors on " + str(p.path)
    p.visitors += random_visitors
    p.change += random_visitors
    if p.visitors < 0:
        p.visitors = 0
    if p.change < 0:
        p.change = 0
    # saving to the DB
    p.save()

    # Five seconds delay in each request
    time.sleep(5)
