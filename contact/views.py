from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Message
from .forms import MessageForm
from django import forms

class MessageListView(ListView):
    message = Message

class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url =  '/'

    #definiujemy metode, która po pozytywnie zwryfikowanych danych zostaje uruchomiona
    def form_valid(self, form):
        form.save() # form jest instancją ModelForm, który posiada metodę "save"
        return super(MessageAddView, self).form_valid(form) # wywołujemy metodę z klasy nadrzędnej i ta metoda zwraca HttpRespnseRedirect(self.get_success_url())
