from django.forms import ModelForm

from June_27_2021.profiles.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
