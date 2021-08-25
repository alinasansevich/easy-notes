from django.db import models


class Note(models.Model):
    """A basic sticky note."""
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.title) > 30:
            return self.title[:30] + "..."
        else:
            return self.title


class ToDoList(models.Model):
    """A checklist note."""
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    text_01 = models.CharField(max_length=100, blank=True)
    text_02 = models.CharField(max_length=100, blank=True)
    text_03 = models.CharField(max_length=100, blank=True)
    text_04 = models.CharField(max_length=100, blank=True)
    text_05 = models.CharField(max_length=100, blank=True)
    text_06 = models.CharField(max_length=100, blank=True)
    text_07 = models.CharField(max_length=100, blank=True)
    text_08 = models.CharField(max_length=100, blank=True)
    text_09 = models.CharField(max_length=100, blank=True)
    text_10 = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.title) > 30:
            return self.title[:30] + "..."
        else:
            return self.title