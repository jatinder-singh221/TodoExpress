from django.shortcuts import render
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

@login_required(login_url='auth:Login')
def account_of_user(request):

    user_details = User.objects.get(id = request.user.id) 
    profile = user_details.linked_profile
    context = {'html_user_details': user_details, 'picture':profile}
    return render(request, 'account.html',context)