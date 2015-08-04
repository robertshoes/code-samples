from django.db import models
from django.forms import ModelForm


"""
first name, last name, phone#, address line 1, city, state, zip)
"""
class Contacts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    address_line = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    
    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)
    


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
    
    

    
