from django import forms
from .models import Book

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'about', 'price','cover')

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'about', 'price','cover')