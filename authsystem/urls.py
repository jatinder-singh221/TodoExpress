from django.urls import path
from .views import login_user,register_user,forget_password_user,user_logout

urlpatterns = [
    path('', login_user, name = 'Login'),
    path('register/', register_user, name = 'Register'),
    path('password/', forget_password_user, name = 'Password'),
    path('logout/', user_logout, name = 'Logout'),
]

app_name = 'authsystem'