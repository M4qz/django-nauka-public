# Projekt Django - Stronka

Testowy projekt Django służący do testowania i prezentacji różnych funkcjonalności frameworka Django.

---

## Opis projektu

Ten projekt to prosta aplikacja Django zawierająca różne widoki i mechanizmy działania, które można testować i rozbudowywać. Wszystkie ścieżki URL dostępne są pod prefiksem `/challange/`.

---

## Dostępne ścieżki URL i ich funkcjonalności

| Ścieżka                        | Opis                                                                                   
|------------------------------- |-----------------------------------------------------------------------------------------------|
| `/challange/simple`            | Widok oparty na klasie `SimpleView`. Wyświetla prostą stronę zdefiniowaną w klasie.           |
| `/challange/simple-taken`      | Widok oparty na klasie `InheritingView`. Dziedziczy funkcjonalności z innego widoku.          |
| `/challange/sesja`             | Wywołuje funkcję `session_example`. Obsługuje sesje użytkownika, np. licznik odwiedzin.       |
| `/challange/`                  | Wywołuje funkcję `club_list`. Wyświetla listę klubów lub inną zawartość.                      | 
| `/challange/index`             | Wywołuje funkcję `template`. Wyświetla zawartość słownika z klubami oraz model z książkami    |
| `/challange/index/<slug:slug>` | Wywołuje funkcję `book_detail`. Pokazuje szczegóły książki na podstawie slug (zamysł jest taki|
|                                | ze jak pojawia sie slug kilka razy to slug jest iterowany od kolejnego rekordu                |
|                                | (toy-story,toy-story-1,toy-story-2).                                                          |
| `/challange/baza/<int:id>`     | Wywołuje funkcję `baza`. Wyświetla dane z bazy na podstawie ID.                               |
| `/challange/inheritance`       | Wywołuje funkcję `inheritance`. Przykład dziedziczenia szablonów w Django.                    |
| `/challange/strona`            | Wywołuje funkcję `html`. Wyświetla stronę HTML zdefiniowaną w widoku.Jest robocza dodana      |
|                                | forma ktora dodaje rekordy do modelu                                                          |
| `/challange/<int:number>`      | Wywołuje funkcję `liczbowy_wywolywacz`. Obsługuje dynamiczne ścieżki z liczbą                 |
                                 |  jako idze słownika klubów.                                                                   |        
| `/challange/<str:name>`        | Wywołuje funkcję `wywolywacz`. Obsługuje dynamiczne ścieżki z nazwą jako parametrem           |
|                                |nazwy klubu.                                                                                   |

---

## Dlaczego istnieje URL `/challange/`?

Ścieżka `/challange/` została dodana w pliku `stronka/stronka/urls.py`, aby przekazać obsługę URLi z głównego projektu (stronka) do aplikacji `projekt`. Dzięki temu wszystkie ścieżki zdefiniowane w `projekt/urls.py` są dostępne pod prefiksem `/challange/`.

---

## Wymagania

- Python  
- Django

---

## Uruchomienie projektu

1. Zainstaluj wymagane zależności:

```bash
pip install -r requirements.txt

2.Uruchom serwer deweloperski i wejdz na http://127.0.0.1:8000/

```bash
python manage.py runserver

**Zobacz na żywo:**  
👉 [**https://django-nauka-li80.onrender.com**](https://django-nauka-li80.onrender.com)


