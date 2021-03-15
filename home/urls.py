from django.urls import path
from .views import index_view,account_of_user

urlpatterns = [
    path('', index_view, name = 'Home'),
    path('account/', account_of_user, name = 'Account'),
]

#app name
app_name = 'home'