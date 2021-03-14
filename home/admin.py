from django.contrib import admin
from .models import extendexd_user_model


@admin.register(extendexd_user_model)
class extended_user_admin(admin.ModelAdmin):
    pass
