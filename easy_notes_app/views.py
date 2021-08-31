from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NoteForm, ToDoListForm
from .models import Note#, ToDoList

def index(request):
    """The home page for Easy Notes."""
    return render(request, 'easy_notes_app/index.html')


def about(request):
    """The about page for Easy Notes."""
    return render(request, 'easy_notes_app/about.html')



def notes(request): # was 'board'
    """The board were all Easy Notes are displayed."""
    notes = Note.objects.order_by('date_added')
    #lists = ToDoList.objects.order_by('date_added')
    context = {'notes': notes,
               #'lists': lists,
               }
    return render(request, 'easy_notes_app/notes.html', context)


def note(request, note_id):
    """Show a single note."""
    note = Note.objects.get(id=note_id)
    context = {'note': note}
    return render(request, 'easy_notes_app/note.html', context) 






def new_note(request):
    """Add a new note."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = NoteForm()
    else:
        # POST data submitted; process data.
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('easy_notes_app:notes')) # board doesn't exist yet!!!
    context = {'form': form}
    return render(request, 'easy_notes_app/new_note.html', context)


def new_list(request):
    """Add a new list."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ToDoListForm()
    else:
        # POST data submitted; process data.
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('easy_notes_app:notes')) # board doesn't exist yet!!!
    context = {'form': form}
    return render(request, 'easy_notes_app/new_list.html', context)


def edit_note(request, note_id):
    """Edit an existing note."""
    
    entry = Note.objects.get(id=note_id)
    
    if request.method != 'POST':
        # Initial request; pre-fillform with the current entry.
        form = NoteForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = NoteForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('easy_notes_app:notes')
    
    context = {'entry': entry,
                'form': form}
    return render(request, 'easy_notes_app/edit_note.html', context)