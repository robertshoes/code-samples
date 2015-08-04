from django.shortcuts import render, get_object_or_404
from shoppinglists.models import TheUser, ShoppingList, ListItem, TheUserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def index(request):
    #After validating the user here make a HttpResponseRedirect    
    if request.method == 'POST':
        form = TheUserForm(request.POST)
        if form.is_valid():            
            user_name = form.cleaned_data['user_name']
            pwd = form.cleaned_data['pwd']
            user = get_object_or_404(TheUser, user_name=user_name)
            
            if user and pwd == user.pwd :
                return HttpResponseRedirect('/shoppinglists/'+str(user.id))
    else:
        form = TheUserForm()
        
    return render(request, 'shoppinglists/index.html', {'form':form})
                  
@login_required(login_url='/shoppinglists/')
def show_list(request, user_id):
    item_list = ShoppingList.objects.filter(user=user_id)
    total = TheUser.objects.get(pk=user_id).get_total_items()    
    context = {'item_list':item_list,'total':total}    
    return render(request, 'shoppinglists/show_item.html', context)
                

    
                
