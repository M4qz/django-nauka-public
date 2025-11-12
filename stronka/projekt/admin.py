from django.contrib import admin
from .models import Book,BookWriter,onetone,manytomany

class  manytomanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
#admin.site.register(Book)
class BookWriterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class onetoneAdmin(admin.ModelAdmin):
        list_display = ('number',)
        search_fields = ('number',)

class BookAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('title',)}  # Automatyczne wypełnianie pola slug na podstawie tytułu
    readonly_fields = ('slug',)  # Pole slug jest tylko do odczytu w panelu admina
    list_filter = ('title','author')
    list_display = ('title','author', 'published_date', 'age','code')  # Wyświetlanie pól w liście
admin.site.register(Book, BookAdmin)
admin.site.register(onetone, onetoneAdmin)
admin.site.register(BookWriter, BookWriterAdmin)
admin.site.register(manytomany, manytomanyAdmin)
# Register your models here.
