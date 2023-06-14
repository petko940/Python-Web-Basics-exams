from django.forms import ModelForm

from February_27_2022.albums.models import Album


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['album_name'].widget.attrs['placeholder'] = 'Album Name'
        self.fields['album_name'].label = 'Album Name'
        self.fields['artist'].widget.attrs['placeholder'] = 'Artist'
        # self.fields['genre'].widget.attrs['placeholder'] = ''
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        self.fields['image_url'].label = 'Image URL'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'
