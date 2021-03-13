from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm


# login of user
def login_user(request):

    if request.method == 'POST':
        post_returned_form = AuthenticationForm(request = request, data = request.POST)

        # checking form 

        if post_returned_form.is_valid():
            get_username = post_returned_form.cleaned_data.get('username')
            get_password = post_returned_form.cleaned_data.get('password')
            let_auth = authenticate(username = get_username, password = get_password)

            # if user is valid then login
            if let_auth is not  None:
                login(request, let_auth)
                return redirect('auth:Test')
            
            # if fail
            else :
                messages.error(request, 'Check Username Or Password')
                
        # if not valid
        else:
            messages.error(request, 'Check Username Or Password')

    login_form = AuthenticationForm()
    context = {'html_login_form': login_form}
    return render(request, 'login.html',context)


# Register of User
def register_user(request):

    if request.method == 'GET':
        register_form = UserCreationForm()

    elif request.method == 'POST':
        print('Register')

    context = {'html_register_form': register_form}
    return render(request,'register.html', context)

# Forget pasword of user
def forget_password_user(request):
    
    if request.method == 'GET':
        passwordchange_form = PasswordChangeForm(request.user)

    elif request.method == 'POST':
        print('forget password')

    context = {'html_resetpassword_form': passwordchange_form}
    return render(request,'password.html', context)


# for testing

def test(request):
    return render(request, 'test.html')