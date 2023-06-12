from django.shortcuts import render, redirect

from August_11_2021.books.models import Book
from August_11_2021.profiles.forms import ProfileForm
from August_11_2021.profiles.models import Profile


# Create your views here.
def profile_page(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    if request.method == 'POST':
        profile.delete()
        books.delete()
        return redirect('home')

    form = ProfileForm(instance=profile)

    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    context = {
        'form': form
    }
    return render(request, 'profiles/delete-profile.html', context)
