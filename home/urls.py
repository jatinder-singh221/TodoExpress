from django.urls import path
from .views import index_view,account_of_user,profile_change,details_update,user_todo,change_details,history,view

urlpatterns = [
    path('', index_view, name = 'Home'),
    path('account/', account_of_user, name = 'Account'),
    path('updateprofile/', profile_change, name = 'Updateprofile'),
    path('updatedetails/', details_update, name='Updatedata'),
    path('add/', user_todo, name = 'Todo'),
    path('changedetails/<int:item_id>/', change_details, name='Change'),
    path('history/', history, name = 'History'),
    path('view/<int:item_id>/', view, name = 'View'),
]

#app name
app_name = 'home'