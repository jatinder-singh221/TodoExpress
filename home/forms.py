from django.forms import ModelForm, models
from .models import extendexd_user_model
from django.contrib.auth.models import User

class extend_user_form(ModelForm):
    class Meta:
        model = extendexd_user_model
        fields = ['user_profile']

class user_detail_form(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name','last_name','email'
        ]