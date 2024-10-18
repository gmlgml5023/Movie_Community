from django.shortcuts import render
from .models import Movie
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
def index(request):
    movies =  get_list_or_404(Movie)
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
