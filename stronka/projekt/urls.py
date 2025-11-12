from django.urls import path
from . import views
from .views import SimpleView, InheritingView
from django.conf import settings
from django.conf.urls.static import static  # poprawny import do media files

urlpatterns = [
    path('simple', SimpleView.as_view(), name='simple'),
    path('simple-taken', InheritingView.as_view(), name='simple-taken'),
    path('sesja', views.session_example, name='sesja'),
    path('', views.club_list),
    path('index', views.template, name='index'),
    path('index/<slug:slug>', views.book_detail, name='index'),
    path('baza/<int:id>', views.baza, name='baza'),
    path('inheritance', views.inheritance),
    path('strona', views.html, name='strona'),
    path('<int:number>', views.liczbowy_wywolywacz),
    path('<str:name>', views.wywolywacz, name='month-challenge'),
]

# Obsługa plików media w trybie DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
urlpatterns = [ #jezeli zostanie wywolana podstrona january ma sie wywolac metoda index z pliku views
path('january',views.essa),
path('february',views.siemka),
path('march',views.bombaclat),
]
'''