from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

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
    # 댓글 폼
    comment_form = CommentForm
    # 댓글 리스트 조회
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)

@login_required
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

@login_required
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

@login_required
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return redirect('movies:index')


@login_required
def comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie_pk)
    context = {
        'movie': movie,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def comments_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user != request.user:
        return HttpResponseForbidden("삭제권한이 없습니다.")
    comment.delete()
    return redirect('movies:detail', movie_pk)
    

@login_required
def likes(request, movie_pk):
    # 좋아요 누를 영화 조회
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')
