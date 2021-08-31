#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 09:32:51 2021

@author: alina
"""

from django import forms

from .models import Note, ToDoList

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title',
                  'text',
                  ]
        labels = {'title': 'Title',
                  'text': '',
                  }
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title',
                  'text_01',
                  'text_02',
                  'text_03',
                  'text_04',
                  'text_05',
                  'text_06',
                  'text_07',
                  'text_08',
                  'text_09',
                  'text_10',
                  ]
        labels = {'Give your list a title': '',
                  'Enter your items here': '',
                  }