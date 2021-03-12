from django.urls import path
from .views import login_user,register_user

urlpatterns = [
    path('', login_user, name = 'Login'),
    path('register/', register_user, name = 'Register'),
]

app_name = 'authsystem'