# Generated by Django 3.1.7 on 2021-03-16 12:41

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_enter_todo_items'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='enter_todo_items',
            managers=[
                ('todo', django.db.models.manager.Manager()),
            ],
        ),
    ]