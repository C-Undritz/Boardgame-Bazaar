from django import forms
from .models import Product, Genre


class ProductForm(forms.ModelForm):

    #  https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        exclude = ('sold', 'stock', 'new_release', 'pre_order')
        # fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(genre.id, genre.get_friendly_name()) for genre in genres]
        genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-1'
