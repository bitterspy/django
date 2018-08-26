from django.utils.html import format_html
from django.db import models

from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    first_name = models.CharField(verbose_name=_("first name"), max_length=20)
    last_name = models.CharField(verbose_name=_("last name"), max_length=50)

    #wyświetla zamiast nazwy klasy, jej pola
    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

    # klasa Meta - tutaj umieszczamy wszystkie dodatkowe informacje
    # poza nazwami pól jak wyżej
    class Meta:
        ordering = ("last_name", "first_name")
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    category = models.CharField(max_length=50)

    def __init__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)
#    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)

    def __str__(self):
        return "{autor} - {tytul}".format(autor=self.author,tytul=self.title)

class BookEdition(models.Model):
    """
    wydanie konkretnej książki
    """
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    date = models.DateField()
    # blank = True oznacza, że nie trzeba wypełniać pola formularza
    isbn = models.CharField(max_length=17, blank=True)

    def __str__(self):
        return "{tytul} {wydawca}".format(tytul=self.title, wydawca = self.publisher)

COVER_TYPES = (
    ('soft','Soft'),
    ('hard','Hard')
)


class BookItem(models.Model):
    """
    Konkretny fizyczny egzemplarz książki
    """
    edition = models.ForeignKey(BookEdition, on_delete=models.PROTECT)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    def __init__(self):
        return "{edition} {cover}".format(edition=self.edition, cover=self.get_cover_type_display())

