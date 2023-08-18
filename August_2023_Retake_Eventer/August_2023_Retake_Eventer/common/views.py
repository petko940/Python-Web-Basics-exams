from django.shortcuts import render
from django.views.generic import TemplateView

from August_2023_Retake_Eventer.accounts.models import ProfileModel


# Create your views here.
class HomeView(TemplateView):
    template_name = 'shared/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_exists = ProfileModel.objects.exists()
        context['profile'] = profile_exists

        return context
