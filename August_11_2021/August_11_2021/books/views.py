from django.shortcuts import render, redirect

from August_11_2021.books.forms import BookForm
from August_11_2021.books.models import Book
from August_11_2021.profiles.models import Profile


# Create your views here.
def add_book(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = BookForm()

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'books/add-book.html', context)


def edit_book(request, pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = BookForm(instance=book)

    context = {
        'profile': profile,
        'form': form,
        'book': book
    }
    return render(request, 'books/edit-book.html', context)


def details_book(request, pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)

    context = {
        'profile': profile,
        'book': book
    }
    return render(request, 'books/book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')
