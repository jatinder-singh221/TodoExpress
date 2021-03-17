from django.forms import ModelForm
from .models import extendexd_user_model,enter_todo_items
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


class todo_entery_form(ModelForm):
    class Meta:
        model = enter_todo_items
        fields = ['todo_name','datetime_to_happen', 'descriptions']