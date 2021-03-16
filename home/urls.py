from django.urls import path
from .views import index_view,account_of_user,profile_change,details_update

urlpatterns = [
    path('', index_view, name = 'Home'),
    path('account/', account_of_user, name = 'Account'),
    path('updateprofile/', profile_change, name = 'Updateprofile'),
    path('updatedetails/', details_update, name='Updatedata')
]

#app name
app_name = 'home'