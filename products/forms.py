"""
Boardgame Bazaar: products App - Forms
"""


from django import forms
from .models import Product, Genre, Review


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    """
    Form that allows the admin user to enter, or displays, product record
    information.
    """
    # Sets the display of genre selection to checkboxes.
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        exclude = ('sold', 'new_release', 'pre_order', 'rating')
        widgets = {'release_date': DateInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(
            genre.id, genre.get_friendly_name()) for genre in genres]
        genres = forms.ModelMultipleChoiceField(
            queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)
        self.fields['genre'].choices = friendly_names


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
