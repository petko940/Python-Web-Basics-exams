from django import forms

from August_2023_Retake_Eventer.events.models import EventModel


class EventModelForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'


class DeleteEventModelForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True

