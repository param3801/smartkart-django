# create form for review rating
from django import forms
from .models import ReviewRating
class ReviewForm(forms.ModelForm):
  class Meta:
    model = ReviewRating
    fields = ['subject', 'review', 'rating']  
    widgets = {
      'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject'}),
      'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review', 'rows': 5}),
      'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Rating'}),
    }
    