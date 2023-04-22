from django.shortcuts import render, redirect

from library.forms import ProfileForm, BookForm
from library.models import Profile, Book


# Create your views here.
def check_if_there_is_profile(request):
    profile = Profile.objects.all()
    if not profile:
        return redirect("home_no_profile")
    else:
        return redirect("home_with_profile")


def home_no_profile(request):
    profile = Profile.objects.all()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_with_profile')
    else:
        form = ProfileForm()

    context = {'form': form, 'profile': profile}
    return render(request, 'home-no-profile.html', context)


def home_with_profile(request):
    profile = Profile.objects.all()[0]
    book = Book.objects.all()
    context = {'profile': profile,
               'book': book}

    return render(request, 'home-with-profile.html', context)


def add_book(request):
    form = BookForm()
    profile = Profile.objects.all()[0]

    context = {'form': form,
               'profile': profile}
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_with_profile')

    return render(request, 'add-book.html', context)


def detail_book(request, id):
    profile = Profile.objects.all()[0]
    book = Book.objects.get(id=id)
    context = {'book': book,
               'profile': profile}

    return render(request, 'book-details.html', context)


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('home_with_profile')


def edit_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)
    profile = Profile.objects.all()[0]

    if form.is_valid():
        form.save()
        return redirect('home_with_profile')

    context = {'form': form,
               'book': book,
               'profile': profile}

    return render(request, 'edit-book.html', context)


def profile(request):
    profile = Profile.objects.all()[0]
    context = {'profile': profile}
    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = Profile.objects.all()[0]

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form,
               'profile': profile}

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]
    books = Book.objects.all()
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        books.delete()
        return redirect('check_if_there_is_profile')

    else:
        for field in form.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

    context = {'profile': profile,
               'books': books,
               'form': form}
    return render(request, 'delete-profile.html', context)


