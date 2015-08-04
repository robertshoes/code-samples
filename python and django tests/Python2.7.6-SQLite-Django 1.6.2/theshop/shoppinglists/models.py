from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput



        
# Create your models here.

class ListItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=300)

    def __unicode__(self):
        return self.item_name


class TheUser(models.Model):
    user_name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    pwd = models.CharField(max_length=100)

    def get_username(self):
        return self.user_name
    
    def get_list_items(self):
        items_per_user = ShoppingList.objects.filter(user=self.pk)
        items_list = []
        for each_item in items_per_user:
            items_list.append(each_item.items.item_name + "-" + each_item.items.item_desc)        
        return items_list
        
    def get_total_items(self):
        qty = 0
        for x in ShoppingList.objects.filter(user=self.pk):
            qty += x.quantity
        return qty

    def __unicode__(self):        
        return self.get_username() 


class ShoppingList(models.Model):
    quantity = models.IntegerField(default=0)
    items = models.ForeignKey(ListItem)
    user = models.ForeignKey(TheUser)

    
    def __unicode__(self):        
        return "Item for user " + str(self.user)

    
#forms

class TheUserForm(ModelForm):
    pwd = PasswordInput()
    class Meta:
        model = TheUser
        exclude = ['lastname', 'email']
