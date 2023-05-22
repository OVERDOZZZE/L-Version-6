import time

from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Books, Author, Publisher
from .forms import BookForm, AddAuthorForm, AddPublisherForm


def books(request):
    books_list = Books.objects.all()
    paginator = Paginator(books_list, 2)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    context = {'books': books}
    return render(request, 'main/books.html', context=context)


def book_detail(request, id):
    book = Books.objects.get(id=id)
    date = date = book.publication_date.strftime("%Y-%m-%d")
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    context = {
        'book': book,
        'date': date,
        'authors': authors,
        'publishers': publishers
               }
    return render(request, 'main/book_detail.html', context=context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'main/add_data.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddAuthorForm()
    return render(request, 'main/add_data.html', {'form': form})


def add_publisher(request):
    if request.method == 'POST':
        form = AddPublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPublisherForm()
    return render(request, 'main/add_data.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Неправильные учетные данные')

    return render(request, 'main/login.html')


def update(request, id):
    book = Books.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = Author.objects.get(id=request.POST.get('author_id'))
        book.publisher = Publisher.objects.get(id=request.POST.get('publisher_id'))
        book.publication_date = request.POST.get('publication_date')

        cover_photo = request.FILES.get('cover_photo')
        if cover_photo:
            filename = '{}_{}'.format(int(time.time()), cover_photo.name)
            filepath = default_storage.save('media/' + filename, cover_photo)
            book.cover_photo = filepath

        book.save()
        return redirect('book_detail', id=id)
