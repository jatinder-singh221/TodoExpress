from django.contrib.auth import authenticate, login, logout
from django.db.models.query import RawQuerySet
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm


# login of user
def login_user(request):
    #redirect if login
    if request.user.is_authenticated:
        return redirect('home:Home')

    else:

        if request.method == 'POST':
            login_form = AuthenticationForm(request= request, data= request.POST)
            # checking form 

            if login_form.is_valid():
                get_username = login_form.cleaned_data.get('username')
                get_password = login_form.cleaned_data.get('password')
                let_auth = authenticate(username = get_username, password = get_password)

                # if user is valid then login
                if let_auth is not  None:
                    login(request, let_auth)

                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                        
                    return redirect('home:Home')
                
                # if fail
                else :
                    messages.error(request, 'Check Username Or Password')
        login_form = AuthenticationForm()
        context = {'html_login_form': login_form}
        return render(request, 'login.html',context)


# Register of User
def register_user(request):

    #redirect if login
    if request.user.is_authenticated:
        return redirect('home:Home')

    else:
        register_form_instance = UserCreationForm
        register_form = register_form_instance(request.POST or None)

        # if request is post
        if request.method == 'POST':

            if register_form.is_valid():
                register_form.save()
                messages.info(request, 'Account created sucessfull')
                return redirect('auth:Login')
            else:
                messages.error(request, 'Enter valid ')

        context = {'html_register_form': register_form}
        return render(request,'register.html', context)


# Forget pasword of user
def forget_password_user(request):

    #redirect if login    
    if request.user.is_authenticated:
        return redirect('home:Home')
        
    return render(request,'password.html')


# logout
def user_logout(request):

    # if login
    if request.user.is_authenticated:
        logout(request)
        return redirect('auth:Login')

    # else if not login
    else:
        return redirect('home:Home')
