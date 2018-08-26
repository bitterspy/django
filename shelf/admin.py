from django.contrib import admin

from .models import Author, Publisher, Book
from rental.models import Rental

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['first_name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']                                               #jakie pole ma slużyć do wyszukiwania
    list_display = ['title']     #jakie kolumny wyświetlać, colored name
                                                                            #daje wartości w kolorze (definicja w models.py)


admin.site.register(Author,AuthorAdmin)                     #rejestruje model i klasę nim zarządzającą
admin.site.register(Book,BookAdmin)
admin.site.register([Publisher])
admin.site.register([Rental])