from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ('title', 'description',)

    def __str__(self):
        return self.title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'        

    def __str__(self):
        return self.content
