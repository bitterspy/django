from django.db import models
from django.contrib.auth.models import User
from shelf.models import BookItem

from django.utils.timezone import now


class Rental(models.Model):
    who = models.ForeignKey(User, on_delete=models.PROTECT)
    what = models.ForeignKey(BookItem, on_delete=models.PROTECT)
    when = models.DateTimeField(default=now)
    #null=True - informacja do bazy danych, że pole może być pust
    #blank=True - informacja dla formularza, że pole moze być puste
    returned = models.DateTimeField(null=True, blank=True)
    def __init__(self):
        return self.what