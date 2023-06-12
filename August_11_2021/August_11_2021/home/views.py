from django.shortcuts import render, redirect

from August_11_2021.books.models import Book
from August_11_2021.profiles.forms import ProfileForm
from August_11_2021.profiles.models import Profile


# Create your views here.
def check_if_there_is_profile(request):
    profile = Profile.objects.all()
    if not profile:
        return no_profile(request)
    else:
        return with_profile(request)


def no_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, 'home/home-no-profile.html', context)


def with_profile(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books
    }
    return render(request, 'home/home-with-profile.html', context)
