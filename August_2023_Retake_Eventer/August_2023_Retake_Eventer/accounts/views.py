from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView

from August_2023_Retake_Eventer.accounts.forms import CreateProfileForm, ProfileEditForm
from August_2023_Retake_Eventer.accounts.models import ProfileModel
from August_2023_Retake_Eventer.events.models import EventModel


# Create your views here.
class CreateProfileView(CreateView):
    template_name = 'profiles/profile-create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('home')


def details_profile(request):
    profile = ProfileModel.objects.all()[0]
    context = {
        'profile': profile,
        'events': EventModel.objects.all()
    }
    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = ProfileModel.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('details_profile')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.all()[0]
    events = EventModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        events.delete()
        return redirect('home')

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile-delete.html', context)
