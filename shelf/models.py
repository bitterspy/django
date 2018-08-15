from django.utils.html import format_html
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    #wyświetla zamiast nazwy klasy, jej pola
    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)

    # funkcja do kolorowania tekstu w tablece
    def colored_name(self):
        return format_html(
            '<span style="color:red;">{} {}</span>',
            self.title,
            self.author,
            self.isbn,
        )

    def __str__(self):
        return "{autor} - {tytul}".format(autor=self.author,tytul=self.title)