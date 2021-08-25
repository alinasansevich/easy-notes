from django.contrib import admin

from easy_notes_app.models import Note, ToDoList

admin.site.register(Note)
admin.site.register(ToDoList)