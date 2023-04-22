from django.forms import ModelForm

from library.models import Profile, Book


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
