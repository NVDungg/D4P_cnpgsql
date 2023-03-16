from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("<uuid:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("<uuid:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("new/", BookCreateView.as_view(), name="book_new"),
    path("search/", SearchResultsListView.as_view(), name="search_results")
]
