from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Добавляем поле для аватарки
    avatar = models.ImageField(upload_to='avatars/', blank=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class File(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
