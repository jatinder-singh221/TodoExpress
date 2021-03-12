from django.urls import path
from .views import login_user,register_user,forget_password_user

urlpatterns = [
    path('login/', login_user, name = 'Login'),
    path('register/', register_user, name = 'Register'),
    path('password/', forget_password_user, name = 'Password'),
]

app_name = 'authsystem'