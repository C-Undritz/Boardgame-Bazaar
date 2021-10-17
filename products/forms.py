from django import forms
from .models import Product, Genre, Review


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    #  https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        exclude = ('sold', 'new_release', 'pre_order', 'rating')
        # fields = '__all__'
        widgets = {'release_date': DateInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(genre.id, genre.get_friendly_name()) for genre in genres]
        genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-1'


class UpdateStockForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('stock',)


class ReviewRateForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'review')


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ('name', 'friendly_name')
