from django.forms import ModelForm

from February_27_2022.profiles.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'
