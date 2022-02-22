from urllib import request
from django.views import generic
from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    #number of visits of homepage
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    # your own name for the list as a template variable
    context_object_name = 'book_list'
    # Specify your own template name/location
    template_name = 'books/book_list.html'
    book_list = Book.objects.all()
    # def get_queryset(self):
    #     # Get 5 books containing the title war
    #     # return Book.objects.filter(title__icontains='war')[:5]
    #     return Book.objects.all()
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        # from django.shortcuts import get_object_or_404
        # book = get_object_or_404(Book, pk=primary_key)

        return render(request, 'books/book_detail.html', context={'book': book})


class AuthorListView(generic.ListView):
    model = Author
    # your own name for the list as a template variable
    context_object_name = 'author_list'
    # Specify your own template name/location
    template_name = 'authors/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author

    def book_detail_view(request, primary_key):
        try:
            book = Author.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Author does not exist')

        return render(request, 'author/author_detail.html', context={'author': author})