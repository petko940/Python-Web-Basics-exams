from django.forms import ModelForm

from June_27_2021.notes.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
