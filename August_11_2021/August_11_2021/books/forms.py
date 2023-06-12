from django.forms import ModelForm

from August_11_2021.books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['image'].widget.attrs['placeholder'] = 'Image'
        self.fields['type'].widget.attrs['placeholder'] = 'Fiction, Novel, Crime'
