from django import forms;
from . import models;

class BookForm(forms.ModelForm) :
    class Meta:
        model = models.Book;
        fields = '__all__';
        exclude = ['id']
        widgets = {
            "authorName": forms.TextInput(attrs={"class": "py-3"}),
            "published": forms.DateInput(attrs={"type": "date"}),
            "bookIntro": forms.Textarea(),
            "authorIntro": forms.Textarea(),
            "notes": forms.Textarea(),
            "reviewd": forms.DateInput(attrs={"type": "date"}),
        }
