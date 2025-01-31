from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    # 사용자가 영화 등록
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 사용자가 영화 좋아요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}. {self.title}'


class Comment(models.Model):
    # 영화에 댓글
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 사용자의 댓글
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content