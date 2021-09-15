from django import forms
from .models import Product, Genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('sold', 'stock', 'new_release', 'pre_order')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(genre.id, genre.get_friendly_name()) for genre in genres]

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-1'
