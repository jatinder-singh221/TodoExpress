from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# indexview
@login_required(login_url = 'auth:Login' )
def index_view(request):
    return render(request, 'test.html')

@login_required(login_url = 'auth:Login' )
def test_view(request):
    return render(request, 'test.html')
