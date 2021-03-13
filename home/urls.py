from django.urls import path
from .views import index_view,test_view

urlpatterns = [
    path('', index_view, name = 'Home'),
    path('test/', test_view, name = 'test'),
]

#app name
app_name = 'home'