#from django.conf.urls import url, include, patterns
from django.urls import path, include
from shelf.views import AuthorListView, AuthorDetailView, BookListView, BookDetailView
app_name = 'shelf'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name = 'author-view'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'), #<int:id> oznacza, że pojawią się cyfry a id to zmienna przekazywana do widoku
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
]