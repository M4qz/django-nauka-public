from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
#from .models import BookWriter  # import modelu autoras
from .models import Book  # import modelu autoras
'''
class ContactForm(forms.Form):
    title = forms.CharField(max_length=100, label='Tytuł książki')

    # tu poprawka — wybór autora jako instancji BookWriter
    author = forms.ModelChoiceField(
        queryset=BookWriter.objects.all(),
        label='Autor',
        required=True
    )

    age = forms.IntegerField(
        label='Wiek',
        validators=[MinValueValidator(1), MaxValueValidator(4)],
        error_messages={
            'min_value': 'Minimalna wartość to 1.',
            'max_value': 'Maksymalna wartość to 4.',
            'required': 'To pole jest wymagane.'
        }
    )
    date = forms.DateField(label='Data')
'''
class ContactForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            "title": "Tytuł książki",
            "author": "Autor",
            "age": "Wiek",
            "date": "Data"
        }
        exclude=['slug','published_countries']
