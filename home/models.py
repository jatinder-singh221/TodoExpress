from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class extendexd_user_model(models.Model):
    linked_user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'User', db_column = 'linked_user', related_name='linked_profile')
    user_profile = models.ImageField(upload_to= 'userprofiles', db_column = 'user_profile', verbose_name = 'Select Profile Picture')

    # manage name   
    extended_user = models.Manager()

    class Meta:
        db_table = 'extended_user'
        verbose_name_plural = 'Extended users'

    def __str__(self):
        return str(self.id)

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):

    # user is created
    if created:
        extendexd_user_model.extended_user.create(linked_user = instance)

@receiver(post_save, sender =User)    
def upate_profile(sender, instance, created, **kwarg):
    
    #if not created
    if created == False:
        pass
        # instance.extendexd_user_model.save()


