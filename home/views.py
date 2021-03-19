from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import extend_user_form, user_detail_form, todo_entery_form
from django.contrib.auth.models import User
from .models import enter_todo_items



# indexview
@login_required(login_url = 'auth:Login' )
def index_view(request):
    profile_of = request.user
    get_query = profile_of.connected_user.all()
    context = {'data':get_query}
    return render(request, 'data.html', context)



@login_required(login_url = 'auth:Login' )
def test_view(request):
    return render(request, 'test.html')


# show user their details
@login_required(login_url='auth:Login')
def account_of_user(request):

    user_details = User.objects.get(id = request.user.id) 
    profile = user_details.linked_profile
    context = {'html_user_details': user_details, 'picture':profile}
    return render(request, 'account.html',context)


# change profile picture
@login_required(login_url= 'auth:Login')
def profile_change(request):

    # if post request 
    profile_of =request.user.linked_profile
    if request.method == "POST":
        profile_of.user_profile.delete()
        post_profile_form = extend_user_form(request.POST, request.FILES, instance=profile_of)

        # if form is valid
        if post_profile_form.is_valid():
            post_profile_form.save()
            messages.success(request, 'profile updated')
            return redirect('home:Account')
        
    profile_form = extend_user_form()

    context = {'html_profile_change_form':profile_form}
    return render(request, 'updateprofile.html', context)
            

# change details
@login_required(login_url={'auth:Login'})  
def details_update(request):
    profile_of =request.user
    
    if request.method == "POST":
        post_form = user_detail_form(request.POST,instance=profile_of)

        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Details updated')
            return redirect('home:Account')

    get_form = user_detail_form(initial={
        'first_name': profile_of.first_name,
        'last_name': profile_of.last_name,
        'email':profile_of.email
    })

    context = {'html_detail_form': get_form}
    return render(request,'updatedetails.html', context)

# enter todo items
@login_required(login_url='auth:Login')
def user_todo(request):

    profile_of = request.user
    todo_form_instance = todo_entery_form
    todo_form = todo_form_instance(request.POST or None)

    if request.method == 'POST':

        if todo_form.is_valid():
            intial_save = todo_form.save(commit=False)
            intial_save.linked_profile = profile_of
            intial_save.save()

            messages.success(request, 'Task Added')
            return redirect('home:Todo')

        else:
            messages.error(request, 'Enter valid data')
    
    context = {'html_todo_form': todo_form }
    return render(request,'todo.html',context)


#change details of todo
@login_required(login_url='auth:Login')
def change_details(request, item_id):
    profile_of = request.user.connected_user.get(id = item_id)

    if request.method == 'POST':
        todo_post = todo_entery_form(request.POST, instance=profile_of)
        if todo_post.is_valid():
            todo_post.save()
            return redirect('home:Home')


    data_get = enter_todo_items.todo.select_related('linked_profile').get(id = item_id)
    todo_change = todo_entery_form(initial=
    {'todo_name':data_get.todo_name, 
    'datetime_to_happen':data_get.datetime_to_happen,
    'descriptions':data_get.descriptions})
    
    context = {'html_todo_change':todo_change, 'of_what':data_get}
    return render(request,'change_todo.html',context)


# history
def history(request):
    profile_of = request.user
    get_query = profile_of.connected_user.all()
    context = {'data':get_query}
    return render(request, 'history.html', context)


# view of todo items
def view(request, item_id):
    
    data_get = enter_todo_items.todo.select_related('linked_profile').get(id = item_id)

    context = {'details':data_get}
    return render(request,'view.html',context)


# completed
def completed(request, item_id):

    data_get = enter_todo_items.todo.select_related('linked_profile').get(id = item_id)
    data_get.isdone = True
    data_get.save()
    return redirect('home:Home')