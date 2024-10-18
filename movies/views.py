from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
def index(request):
    # 전체 영화 조회
    movies =  get_list_or_404(Movie)
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    # 단일 영화 조회
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


def create(request):
    # POST 요청이면
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():  # 유효성 검사
            movie = form.save(commit=False)
            movie.user = request.user  # 현재 로그인한 사용자 할당
            movie.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)


def update(request, movie_pk):
    # 수정할 단일 영화 조회
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)


def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return redirect('movies:index')