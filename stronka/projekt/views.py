from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect,Http404
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from .forms import ContactForm
from .models import Book
from django.template.loader import render_to_string
#from .forms import ContactForm
from django.views.generic.base import TemplateView

clubs={
    "barcelona":"najlepszy klub",
    "madryt":"nie lubie ;)",
    "atletico":"oby drudzy",
    "elche":None
}



def session_example(request):
    if request.method == "POST":
        request.session.flush()
        return redirect(reverse("sesja"))

    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    return render(request, "session_example.html", {"counter": request.session['counter']})


def inheritance(request):
        strona_bs=None
        is_valid=None
        if request.method == 'POST':
            strona = request.POST.get('strona')
            strona_bs="".join(strona.split())
            if strona_bs=="":
                is_valid=False
            else:
                is_valid=True
        return render(request, 'main.html', {'strona_bs': strona_bs,'is_valid':is_valid})

def template(request):
    books=Book.objects.all()
    return render(request, 'index.html', {'clubs': clubs, 'books': books})


def club_list(request):
    klucze = list(clubs.keys())
    lista = ''
    for i in range(len(klucze)):
        sciezka = reverse('month-challenge', args=[klucze[i]])
        lista += f"<li><a href='{sciezka}'>{klucze[i].capitalize()}</a></li>"
    return HttpResponse(f"<ul>{lista}</ul>")

def wywolywacz(request,name):
    try:
     data=clubs[name]
     if data:
      result=f"<h1>{data}</h1>"
     else:
         result = f"<h1>{'jeszcze nie w laliga'}</h1>"
     return HttpResponse(result)
    except:
        return HttpResponseNotFound("<h1>nie ma takiego klubu</h1>")

def liczbowy_wywolywacz(request,number):
    try:
     klucze=list(clubs.keys())
     #print(klucze)
     nazwa=klucze[number-1]
     sciezka=reverse('month-challenge',args=[nazwa])
     return HttpResponseRedirect(sciezka)
    except:
       raise Http404()

def html(request):
    word = 'jamaican'
    form=ContactForm()
    #message_max = form.fields['message'].error_messages['max_length']
    #message_max = list(form.fields['message'].error_messages.values())
    #print(message_max)

    # Ręczne dodanie błędów do pola message z error_messages zdefiniowanych w formularzu
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['title']
            author = form.cleaned_data['author']  # już jest instancja BookWriter
            age = form.cleaned_data['age']
            date = form.cleaned_data['date']
            model=Book(title=name,author=author,published_date=date,age=age)
            model.save()
            return HttpResponse(f"Dziękujemy za wiadomość, {name}! Odpowiemy na {author} z treścią: {age}{date}")
        else:
            # Jeżeli są inne błędy (lub ponownie dodajemy te ręczne), przekazanie formularza z błędami
            return render(request, 'strona_glowna.html', {'bomboclat': word, 'form': form})
    else:
        form = ContactForm(request.POST)
        #form.add_error('message', form.fields['message'].error_messages['max_length'])
       # form.add_error('message', form.fields['message'].error_messages['required'])
    return render(request, 'strona_glowna.html', {'bomboclat': word, 'form': form})


def baza(request,id):
    books = Book.objects.get(pk=id)#pk jest kluczem glownym tabeli(w tym przypadku jest to id)
    return render(request, 'baza.html', {
        'title': books.title,
        'author': books.author,
        'published_date': books.published_date,
        'age': books.age})

def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
        result = f"<h1>{book}</h1>"
        return HttpResponse(result)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

class SimpleView(TemplateView):
    template_name = "klasa_view.html"

    def get_context_data(self, **kwargs):
        # najpierw pobierz kontekst od rodzica
        context = super().get_context_data(**kwargs)
        # dodaj swoją zmienną
        #context["is_valid"] = "jamaican"
        #print(context["is_valid"])
        return context


class InheritingView(SimpleView):
    template_name = "klasa_view.html"  # możesz używać tego samego albo innego szablonu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # dziedziczymy wszystko z SimpleView
        context["is_valid"] = "hejka"  # nadpisujemy zmienną
        return context