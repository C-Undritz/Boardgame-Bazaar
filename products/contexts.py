"""
Boardgame Bazaar: products App - Contexts
"""


from .models import Genre


def genres_list(request):
    """
    Provides the genre objects throughout the site for the 'shop by genre'
    drop down navbar menu
    """
    genres = Genre.objects.all().order_by('friendly_name')

    context = {
        'genres': genres,
    }

    return context
