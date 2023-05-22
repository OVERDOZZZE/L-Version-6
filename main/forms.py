from django import forms
from .models import Author, Publisher, Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'publisher', 'publication_date', 'cover_photo']


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']


class AddPublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address']
