from django.forms import ModelForm
from .models import extendexd_user_model

class extend_user_form(ModelForm):
    class Meta:
        model = extendexd_user_model
        fields = ['user_profile']