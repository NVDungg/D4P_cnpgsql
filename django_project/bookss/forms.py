from django import forms
from .models import Book, Review

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','author', 'about', 'price','cover')

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'about', 'price','cover')

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)