from django.db import models

class Post(models.Model):
     title = models.CharField(max_length=255)
     slug = models.SlugField(unique=True)
     intro = models.TextField()
     body = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          ordering = ['-created_at',]

class Comment(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
     name = models.CharField(max_length=255)
     email = models.EmailField()
     body = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)