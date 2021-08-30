from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NoteForm, ToDoListForm


def index(request):
    """The home page for Easy Notes."""
    return render(request, 'easy_notes_app/index.html')


def about(request):
    """The about page for Easy Notes."""
    return render(request, 'easy_notes_app/about.html')


def board(request):
    """The board were all Easy Notes are displayed."""
    return render(request, 'easy_notes_app/board.html')

    
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
            return HttpResponseRedirect(reverse('easy_notes_app:board')) # board doesn't exist yet!!!
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
            return HttpResponseRedirect(reverse('easy_notes_app:board')) # board doesn't exist yet!!!
    context = {'form': form}
    return render(request, 'easy_notes_app/new_list.html', context)


