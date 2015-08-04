from django.db import models

# Create your models here.
"""
DB design

Domain
id   PK
domain_name vachar(100) --> will contain the domain's name. Ex. "http://www.gizmodo.com"


Page
id       PK
i        varchar(300) --> will contain the title of the page.  Ex. "A article"
path     varchar(300) --> will contain the path to the page. Ex. "/year/month/a-article"
visitors number       --> will contain the number of visitors
change   number       --> will contain the delta of visitors from 5 seconds to actual time(|visitors_now - visitors_5_secs_ago|)
domain_id FK(Domain.id)
"""

class Domain(models.Model):
    #name of the domain
    domain_name = models.URLField(max_length=100)


    def __unicode__(self):
        return self.domain_name

class Page(models.Model):
    i = models.CharField(max_length=300, verbose_name="title")
    path = models.CharField(max_length=300)
    visitors = models.IntegerField(default=0)
    change = models.IntegerField(default=0)
    domain_id = models.ForeignKey(Domain)


    def __unicode__(self):
        return str(self.i)
