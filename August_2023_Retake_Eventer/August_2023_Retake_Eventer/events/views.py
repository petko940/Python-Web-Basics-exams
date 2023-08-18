from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from August_2023_Retake_Eventer.accounts.models import ProfileModel
from August_2023_Retake_Eventer.events.forms import EventModelForm, DeleteEventModelForm
from August_2023_Retake_Eventer.events.models import EventModel


# Create your views here.
class DashboardPageView(TemplateView):
    template_name = 'events/dashboard.html'
    model = EventModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_exists = ProfileModel.objects.exists()
        context['profile'] = profile_exists
        context['events'] = self.model.objects.all()
        return context


class CreateEventView(CreateView):
    template_name = 'events/event-create.html'
    form_class = EventModelForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_exists = ProfileModel.objects.exists()
        context['profile'] = profile_exists
        return context


class EventDetailsView(DetailView):
    template_name = 'events/events-details.html'
    model = EventModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = EventModel.objects.get(pk=self.kwargs['pk'])
        profile_exists = ProfileModel.objects.exists()
        context['profile'] = profile_exists
        return context


class EditEventView(UpdateView):
    model = EventModel
    template_name = 'events/event-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_exists = ProfileModel.objects.exists()
        context['profile'] = profile_exists
        return context


class DeleteEventView(DeleteView):
    model = EventModel
    template_name = 'events/events-delete.html'
    success_url = reverse_lazy('dashboard')
    form_class = DeleteEventModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_exists = ProfileModel.objects.exists()
        context['profile'] = profile_exists
        context['form'] = DeleteEventModelForm(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()  # Manually delete the object
        return HttpResponseRedirect(self.success_url)
