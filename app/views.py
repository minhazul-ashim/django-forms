from django.shortcuts import render
from django.http import HttpResponse;
from . import forms;
from . modelForms import BookForm;

# Create your views here.
def index(request) :
    form = forms.contactForm;
    bookForm = BookForm;
    return render(request, 'form.html', { 'form': form, 'bookForm': bookForm });

# def dForm(request) :
#     return render(request, './form.html')