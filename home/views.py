from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import extend_user_form 


# indexview
@login_required(login_url = 'auth:Login' )
def index_view(request):
    return render(request, 'index_base.html')



@login_required(login_url = 'auth:Login' )
def test_view(request):
    return render(request, 'test.html')

def account_of_user(request):

    extend_form = extend_user_form()
    context = {'html_extended_user_form' :extend_form}

    return render(request, 'test.html',context)