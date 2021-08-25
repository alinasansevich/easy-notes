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
    # Board page
    # path('board/', views.board, name='board'),
    ]