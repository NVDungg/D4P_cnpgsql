from .models import Book
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import EditBookForm, CreateBookForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"             #redirec to login if not logged

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = ("books.special_status", )

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = "books/book_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = EditBookForm
    template_name = "books/book_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author_review == self.request.user

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = "book_list"

    def test_func(self):
        obj = self.get_object()
        return obj.author_review == self.request.user
    
class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
