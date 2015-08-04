from django.contrib import admin
from shoppinglists.models import ListItem, ShoppingList, TheUser

# Register your models here.

admin.site.register(ListItem)
admin.site.register(ShoppingList)
admin.site.register(TheUser)

