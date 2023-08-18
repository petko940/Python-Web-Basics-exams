from django import forms

from August_2023_Retake_Eventer.accounts.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = [
            'email',
            'profile_picture',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(CreateProfileForm):
    class Meta(CreateProfileForm.Meta):
        fields = "__all__"
