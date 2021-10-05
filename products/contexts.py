from .models import Genre


def genres_list(request):
    genres = Genre.objects.all().order_by('friendly_name')

    context = {
        'genres': genres,
    }

    return context
