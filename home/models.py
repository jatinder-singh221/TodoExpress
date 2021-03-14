from django.db import models
from django.contrib.auth.models import User

class extendexd_user_model(models.Model):
    linked_user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'User', db_column = 'linked_user')
    user_profile = models.ImageField('User Image', upload_to= 'userprofiles', db_column = 'user_profile')

    # manage name   
    extended_user = models.Manager()

    class Meta:
        db_table = 'extended_user'
        verbose_name_plural = 'Extended users'
