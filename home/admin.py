from django.contrib import admin
from .models import extendexd_user_model,enter_todo_items


@admin.register(extendexd_user_model)
class extended_user_admin(admin.ModelAdmin):
    pass

@admin.register(enter_todo_items)
class todo_admin(admin.ModelAdmin):
    list_display = ['todo_name','datetime_to_happen']
    list_display_links = ['todo_name']