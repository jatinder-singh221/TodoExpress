from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import extend_user_form, user_detail_form 
from django.contrib.auth.models import User



# indexview
@login_required(login_url = 'auth:Login' )
def index_view(request):
    return render(request, 'index_base.html')



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
