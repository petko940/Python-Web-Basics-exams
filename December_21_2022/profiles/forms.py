from django.forms import ModelForm

from profiles.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
