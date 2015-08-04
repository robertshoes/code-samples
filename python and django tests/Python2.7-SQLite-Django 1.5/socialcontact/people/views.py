# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from people.models import Contacts, ContactsForm
from django.template import RequestContext
        
"""
This is just a test project in Django's
lastest version 1.4.1
What it does is show a sqllite DB of one
table that shows contacts per page and you
create, update, edit or delete them.

UPDATE: The latest release of Django is
1.5
"""


def list_contact(request, start=0,end=0):
    #Using an algorithm created by me for
    #pagination.
    back = False
    back_start = ''
    back_end = ''
    forward = True
    counter = len(Contacts.objects.all())
    if request.GET:        
        end = int(request.GET['end'])
        start = int(request.GET['start'])
        all_contacts = Contacts.objects.all()[start:end]
        if len(all_contacts) < 3 or (end >= counter):
            forward = False
        else:
            forward = True        
        first_time = 0    
        if start <= 0:
            back_start = 1
            back_end = 4
            back = False            
        else:
            back_start = start - 3
            back_end = end - 3
            back = True
            
    else:
        all_contacts = Contacts.objects.all()[1:4]
        first_time = 1
        
    if counter > 3:
            start = int(start) + 3
            end = start + 3        
            
    return render_to_response('list_contact.html', {'contacts': all_contacts, 'start':start,'end':end, 
                                'first_time':first_time, 'back_start':back_start,'back_end':back_end, 'back':back, 'forward':forward, 'counter':counter})
    
def new_contact(request):
    #Checking for POST request and validation the form
    if request.POST:        
        contactsForm = ContactsForm(request.POST)        
        if contactsForm.is_valid():
            #saving the contact to the DB
            contactsForm.save()
            return render_to_response('add_contact.html', {'added': True, 'first_name': request.POST['first_name'], 'last_name': request.POST['last_name']}, context_instance=RequestContext(request))    
    else:        
        contactsForm = ContactsForm()          
    
    return render_to_response('add_contact.html', {'contactsForm': ContactsForm, 'added': False}, context_instance=RequestContext(request))
    

    
def edit_contact(request, contact_id):
    #valid contact since is part of the URL
    #TODO: needs validation in order to avoid directly manipulation
    #of the URL through the browser or a program
    form = Contacts.objects.get(pk=contact_id)
    if request.POST:        
        contactsForm = ContactsForm(request.POST, instance=form)
        if contactsForm.is_valid():            
            contactsForm.save()
            return render_to_response('edit_contact.html', {'added': True, 'first_name': request.POST['first_name'], 'last_name': request.POST['last_name']})
    
    else:
        #Passing the form to the ContacsForm class in order
        #to populate the fields of thee web form
        contactsForm = ContactsForm(instance=form) 
        
    return render_to_response('edit_contact.html', {'contactsForm': contactsForm, 'added': False, 'first_name': form.first_name, 'last_name': form.last_name}, context_instance=RequestContext(request))
    
    
def search_contact(request):
    #Search for contacts based on their names
    search = False
    all_contact = False
    counter = False
    if request.POST:
        all_contact = Contacts.objects.filter(first_name__startswith=request.POST['first_name']).filter(last_name__startswith=request.POST['last_name'])
        search = True
        counter = len(all_contact)
    contactsForm = ContactsForm()
    return render_to_response('list_contact.html', {'contacts':all_contact,'contactsForm':contactsForm, 'search':search, 'counter':counter}, context_instance=RequestContext(request))
