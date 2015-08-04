__author__ = 'RZapata'

from rest_framework import serializers
from concurrents_increase.models import Domain, Page



class PageSerializer(serializers.ModelSerializer):
    #This class helps make the connection between the model
    #and what fields I want to show in the response
    class Meta:
        model = Page
        fields = ("i", "path", "visitors", "domain_id")

class PageSerializerIncrease(serializers.ModelSerializer):
    #This class helps make the connection between the model
    #and what fields I want to show in the response
    class Meta:
        model = Page
        fields = ("i", "path", "change")


class DomainSerializer(serializers.ModelSerializer):
    #This class helps make the connection between the model
    #and what fields I want to show in the response
    class Meta:
        model = Domain
        fields = ("domain_name",)