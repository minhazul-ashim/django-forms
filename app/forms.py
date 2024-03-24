from django import forms;
import datetime

class contactForm(forms.Form) :
    name = forms.CharField(min_length=8)

    comment = forms.CharField(widget=forms.Textarea, required=False)

    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    email = forms.EmailField(label='Please Enter your valid email address')

    agree = forms.BooleanField(initial=True)

    dateTime = forms.CharField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))

    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    BIRTH_YEAR_CHOICES = [('S', '1980'), ('S', '1990')]

    birth_year = forms.DateField(widget=forms.RadioSelect(choices=BIRTH_YEAR_CHOICES))

    value = forms.DecimalField(min_value=5, max_value=100)

    today_Date = forms.CharField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), initial=datetime.date.today)

    Footballers = [('R', 'Ronaldo'), ('M', 'Messi'),( 'D', 'Dybala')]

    favoriteFootballer = forms.CharField(widget=forms.Select(choices=Footballers))

    Footballers = [('R', 'Ronaldo'), ('M', 'Messi'),( 'D', 'Dybala')]

    MultipleFootballers = forms.CharField(widget=forms.SelectMultiple(choices=Footballers))
