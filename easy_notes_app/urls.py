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
    path('board/', views.board, name='board'),
    ]