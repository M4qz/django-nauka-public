# Projekt Django – Stronka  
**Testowy projekt Django** służący do eksperymentowania i prezentacji kluczowych funkcjonalności frameworka.

---

## Opis projektu
Prosta aplikacja Django demonstrująca różnorodne widoki, mechanizmy sesji, szablony oraz dynamiczne URL-e.  
Wszystkie ścieżki dostępne są pod wspólnym prefiksem **`/challange/`**.

---

## Dostępne ścieżki URL i ich funkcjonalności

| Ścieżka | Opis |
|--------|------|
| `/challange/simple` | Klasa `SimpleView` – podstawowy widok renderujący statyczną stronę. |
| `/challange/simple-taken` | Klasa `InheritingView` – przykład dziedziczenia po innym widoku. |
| `/challange/sesja` | Funkcja `session_example` – obsługa sesji (np. licznik odwiedzin). |
| `/challange/` | Funkcja `club_list` – lista klubów lub domyślna zawartość. |
| `/challange/index` | Funkcja `template` – renderowanie szablonu z danymi klubów i modelami książek. |
| `/challange/index/<slug:slug>` | Funkcja `book_detail` – szczegóły książki na podstawie `slug`. <br>**Uwaga:** przy duplikacie `slug` system automatycznie iteruje (np. `toy-story`, `toy-story-1`, `toy-story-2`). |
| `/challange/baza/<int:id>` | Funkcja `baza` – pobieranie i wyświetlanie rekordu z bazy po ID. |
| `/challange/inheritance` | Funkcja `inheritance` – demonstracja dziedziczenia szablonów. |
| `/challange/strona` | Funkcja `html` – w pełni funkcjonalna strona z formularzem dodającym rekordy do modelu. |
| `/challange/<int:number>` | Funkcja `liczbowy_wywolywacz` – dynamiczna ścieżka z liczbą jako kluczem do słownika klubów. |
| `/challange/<str:name>` | Funkcja `wywolywacz` – dynamiczna ścieżka z nazwą klubu jako parametrem. |

---

## Dlaczego istnieje prefiks `/challange/`?
Ścieżka została zdefiniowana w pliku **`stronka/stronka/urls.py`**, aby delegować wszystkie żądania do aplikacji `projekt`.  
Dzięki temu wszystkie URL-e zdefiniowane w `projekt/urls.py` są dostępne pod wspólnym prefiksem.

---

## Wymagania
- Python 3.8+
- Django 4.x+

---

## Uruchomienie projektu

```bash
# 1. Zainstaluj zależności
pip install -r requirements.txt

# 2. Uruchom serwer deweloperski
python manage.py runserver
```

**Dostęp lokalny:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

**Zobacz na żywo:**  
👉 [**https://django-nauka-li80.onrender.com**](https://django-nauka-li80.onrender.com)
