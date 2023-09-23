from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class Author(models.Model):
    name = models.CharField(max_length=50,unique=True)  
    bio = models.CharField(max_length=200)

class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True)

class Novel(models.Model):
    title = models.TextField(unique=True)
    cover = models.TextField(null=True, blank=True)
    total_likes = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='On-going')
    description = models.TextField(null=True, blank=True)
    published_time = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=5.0)
    authors = models.ManyToManyField(Author, through='NovelAuthor')
    genres = models.ManyToManyField(Genre, through='NovelGenre')

class NovelAuthor(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('novel', 'author'),)

class NovelGenre(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('novel', 'genre'),)

class Chapter(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    title = models.TextField()
    path = models.TextField(unique=True) 
    chapter_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        index_together = (('novel', 'chapter_number'),)

class Comment(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = (('novel', 'user'),)