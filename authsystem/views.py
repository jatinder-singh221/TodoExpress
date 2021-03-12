from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm

# login of user
def login_user(request):

    if request.method == 'GET':
        login_form = AuthenticationForm()

    elif request.method == 'POST':
        print('hi')

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