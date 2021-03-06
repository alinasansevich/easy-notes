#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:25:05 2021

@author: alina

Defines URL patterns for easy_notes_app.
"""

from django.urls import path
from . import views

app_name = "easy_notes_app"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # About page
    path('about/', views.about, name='about'),
    # Page for adding a new note
    path('new_note/', views.new_note, name='new_note'),
    # Page for adding a new list
    path('new_list/', views.new_list, name='new_list'),
    # Board page
    path('notes/', views.notes, name='notes'),
    # Page to show a note
    path('note/<int:note_id>', views.note, name='note'),
    # Page for editing a note
    path('edit_note/<int:note_id>', views.edit_note, name='edit_note'),
    # Page to show a list
    # path('lista/<int:lista_id>', views.lista, name='lista'),
    ]