from .models import Book
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from .forms import EditBookForm, CreateBookForm, CreateReviewForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"             #redirec to login if not logged

class BookDetailView(LoginRequiredMixin, View):    #PermissionRequiredMixin,
    login_url = "account_login"
    #permission_required = ("books.special_status", )

    def get(self, request, *args, **kwargs):
        view = ReviewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReviewPost.as_view()
        return view(request, *args, **kwargs)

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = "books/book_create.html"

    def form_valid(self, form):
        form.instance.author_review = self.request.user
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
    

class ReviewGet(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateReviewForm()
        return context

class ReviewPost(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Book
    form_class = CreateReviewForm
    template_name = "books/book_detail.html"

    def post(self, request, *args, **kwargs):
        """grab the book pk from the URL"""
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        form.instance.author = self.request.user    ##set author it instance the one who create comment
        comment.book = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})    



class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
