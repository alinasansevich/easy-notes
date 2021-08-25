from django.shortcuts import render


def index(request):
    """The home page for Easy Notes."""
    return render(request, 'easy_notes_app/index.html')


def about(request):
    """The about page for Easy Notes."""
    return render(request, 'easy_notes_app/about.html')


# def board(request):
