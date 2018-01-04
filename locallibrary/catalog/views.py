from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_intances = BookInstance.objects.count()

    # Available books an “exact” match.(status = 'a')
    num_intances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.all().count()	# The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', locals())


def BookListView(request):
    book_list = Book.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(book_list, 9)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'book_list.html', locals())


@login_required
def book_detail_view(request, pk):
    try:
        book = Book.objects.get(id = pk)
    except Book.DoesNotExist:
        raise Http404('Book does not exist!')

    return render(request, 'book_detail.html', locals())




def AuthorListView(request):
    author_list = Author.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(author_list, 3)

    try:
        authors = paginator.page(page)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)
    return render(request, 'author_list.html', locals())